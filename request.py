import requests

r = requests.get("https://boardgamegeek.com/xmlapi2/thing?type=boardgame&id=174430")

print(r.text)
