import xml.etree.ElementTree as ET
import database


def add_collection_to_database(database_, xml_root, username):
    root = ET.fromstring(xml_root)
    for element in root:
        bg_id = element.attrib['objectid']
        user_rating = element.find('stats').find('rating').attrib['value']
        if user_rating == 'N/A':
            user_rating = 0
        database_.query(
            "INSERT INTO bg_collection(username,bg_id,rating) VALUES(%s,%s,%s) ON CONFLICT(username,bg_id) DO UPDATE SET rating=%s;",
            (username, bg_id, user_rating, user_rating,))

def add_similar_games_to_database(database_, similar_games):
    for bg_id in similar_games:
        for sg_id in similar_games.get(bg_id):
            database_.query(
                "INSERT INTO bg_similar(bg_id,similargame_id) VALUES(%s,%s) ON CONFLICT(bg_id,similargame_id) DO NOTHING;",
                (bg_id,sg_id,)
            )
