from database import Database
import webscrape
import api_request
import util

"""
Generates a weighted list of recommended games based on a user's collection on BGG.

Assumptions:
    - Device running code has locally running PostgreSQL server
    - Database 'mydb' has been generated with appropriately formatted tables as found in bgg_tables.txt
    - User exist on boardgamegeek.com and has a public collection with 1+ rated board game(s)
"""

db = Database()

# Get user collection data and store it in the database
user_name = input("Enter user name: ")
xml_root = api_request.get_collection_for_user(user_name)
util.add_collection_to_database(db,xml_root,user_name)

# Get all board games in user's collection and trim out any rated 0
result = db.select_query("SELECT c.bg_id,c.rating FROM bg_collection c INNER JOIN boardgame bg ON c.bg_id = bg.id WHERE c.username=%s;",(user_name,))
bg_ids = []
for item in result:
    if item['rating'] > 0:
        bg_ids.append(item['bg_id'])

# Create a subset list of board games which haven't had similar games already scrapped from BGG
webscrape_ids = bg_ids.copy()
result = db.select_query("SELECT bg_id,COUNT(bg_id) as count FROM bg_similar GROUP BY bg_id;")
for item in result:
    if item['count'] > 0:
        bg_id = item['bg_id']
        if bg_id in webscrape_ids:
            webscrape_ids.remove(bg_id)

# Scrape data from web into database for similar games
similar_games = webscrape.get_fans_also_like_for(webscrape_ids)
util.add_similar_games_to_database(db,similar_games)


# Run a rudimentary algorithm to assign a weight to each recommended game
weighted_list = {}
orig_game_ids = {}
for bg_id in bg_ids:
    result = db.select_query("SELECT sg.similargame_id,bg.bayesaverage,c.rating FROM boardgame bg INNER JOIN bg_similar sg ON bg.id=sg.similargame_id INNER JOIN bg_collection c ON c.bg_id = sg.bg_id WHERE c.username=%s AND sg.bg_id=%s AND sg.similargame_id NOT IN (SELECT bg_id FROM bg_collection WHERE username=%s);",(user_name,bg_id,user_name,))
    for item in result:
        sg_id = int(item['similargame_id'])
        sg_rating = float(item['bayesaverage'])
        user_bg_rating = float(item['rating'])

        # Multiplying the user's rating for the original board game against the average rating for the similar board game.
        # Will take average if multiple board games have the same recommended similar board game.
        # Note: Average is not actually calculated correctly, later games will have more weight with current algorithm.
        weighted_list.setdefault(sg_id,sg_rating * user_bg_rating)
        weighted_list[sg_id] = (weighted_list[sg_id] + sg_rating * user_bg_rating)/2
        orig_game_ids.setdefault(sg_id, [])
        orig_game_ids[sg_id].append(bg_id)

# Print out the recommended games with their associated weights.
for sg_id in sorted(weighted_list,key=weighted_list.get):
    result = db.select_query("SELECT name FROM boardgame WHERE id=%s",(sg_id,))

    # Only show results for games that appear in recommended similar board games 2+ times
    if len(orig_game_ids[sg_id]) >= 2:
        print (str(sg_id) + ' : ' + result[0]['name'] + ' - ' + str(weighted_list[sg_id]) + ' - ' + str(orig_game_ids[sg_id]))

db.close()