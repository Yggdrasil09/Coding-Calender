import requests
import bs4
import json

with open('sites.json') as f:
    data = json.load(f)

competitions = open("competitons.txt","w")

for x in data:
    competitions.write(x+'\n')



