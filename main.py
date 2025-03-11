from database import Database
import webscrape
import api_request
import util

db = Database()

# user_name = input("Enter user name: ")
user_name = 'Dynzad'
xml_root = api_request.get_collection_for_user(user_name)
util.add_collection_to_database(db,xml_root,user_name)
result = db.select_query("SELECT c.bg_id,c.rating,bg.name FROM bg_collection c INNER JOIN boardgame bg ON c.bg_id = bg.id WHERE c.username=%s;",(user_name,))

bg_ids = []
for item in result:
    bg_ids.append(item['bg_id'])

webscrape_ids = bg_ids.copy()
result = db.select_query("SELECT bg_id,COUNT(bg_id) as count FROM bg_similar GROUP BY bg_id;")
for item in result:
    if item['count'] > 0:
        bg_id = item['bg_id']
        if bg_id in webscrape_ids:
            webscrape_ids.remove(bg_id)

similar_games = webscrape.get_fans_also_like_for(webscrape_ids)
util.add_similar_games_to_database(db,similar_games)

weighted_list = {}
for bg_id in bg_ids:
    result = db.select_query("SELECT sg.similargame_id,bg.bayesaverage,c.rating FROM boardgame bg INNER JOIN bg_similar sg ON bg.id=sg.similargame_id INNER JOIN bg_collection c ON c.bg_id = sg.bg_id WHERE c.username=%s AND sg.bg_id=%s AND sg.similargame_id NOT IN (SELECT bg_id FROM bg_collection WHERE username=%s);",(user_name,bg_id,user_name,))
    for item in result:
        sg_id = int(item['similargame_id'])
        sg_rating = float(item['bayesaverage'])
        user_bg_rating = float(item['rating'])
        weighted_list.setdefault(sg_id,0)
        weighted_list[sg_id] = weighted_list[sg_id] + sg_rating * user_bg_rating



for sg_id in sorted(weighted_list,key=weighted_list.get):
    result = db.select_query("SELECT name FROM boardgame WHERE id=%s",(sg_id,))
    print (str(sg_id) + ' : ' + result[0]['name'] + ' - ' + str(weighted_list[sg_id]))

db.close()