import json
from pprint import pprint

with open('trafficCapture.json') as f:
    data = json.load(f)

pprint(data)