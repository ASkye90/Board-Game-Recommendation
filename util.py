import xml.etree.ElementTree as ET

def add_collection_to_database(database_, xml_text, username):
    """
    Adds a user collection to SQL table bg_collection

    :param database_: Database to add data into
    :param xml_text: XML-formatted string of user collection from BGG XML API2
    :param username: Name of user
    """
    root = ET.fromstring(xml_text)
    for element in root:
        bg_id = element.attrib['objectid']
        user_rating = element.find('stats').find('rating').attrib['value']
        if user_rating == 'N/A':
            user_rating = 0
        database_.query(
            "INSERT INTO bg_collection(username,bg_id,rating) VALUES(%s,%s,%s) ON CONFLICT(username,bg_id) DO UPDATE SET rating=%s;",
            (username, bg_id, user_rating, user_rating,))

def add_similar_games_to_database(database_, similar_games):
    """
    Add similar games to SQL table bg_similar

    :param database_: Database to add data into
    :param similar_games: (Dict of int: [int])
                            Key: id for original board game
                            Values: List of ids for similar board games
    """
    for bg_id in similar_games:
        for sg_id in similar_games.get(bg_id):
            database_.query(
                "INSERT INTO bg_similar(bg_id,similargame_id) VALUES(%s,%s) ON CONFLICT(bg_id,similargame_id) DO NOTHING;",
                (bg_id,sg_id,)
            )
