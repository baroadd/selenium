import json
from pprint import pprint

with open('trafficCapture.json') as f:
    data = json.load(f)
    for i in data.values():
        pprint(data["log"]["entries"][0]["request"]["url"])
# pprint(data["log"]["entries"][0]["request"]["url"])