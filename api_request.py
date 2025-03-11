import time

import requests

def get_collection_for_user(user):
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