import time

import requests

def get_collection_for_user(user):
    """
    Get the API collection data for a given user on BGG

    :param user: Username on BGG
    :return: Raw XML text for user collection from BGG XML API2
    """
    coll = {}
    while True:
        r = requests.get(
            f"https://boardgamegeek.com/xmlapi2/collection?username={user}&excludesubtype=boardgameexpansion&stats=1&brief=1")
        status = r.status_code
        if status == 202:
            time.sleep(3)
            continue
        break

    return r.text