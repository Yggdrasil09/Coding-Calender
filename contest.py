import requests
import bs4
import json

with open('sites.json') as f:
    data = json.load(f)

competitions = open("competitons.txt","w")

for x in data:
    competitions.write(x+'\n')
    if x == "Codechef":
        headers = {'user-agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Mobile Safari/537.36' }
        res = requests.get(data[x],headers=headers)
    # print(res.text[:5000])
    try:
        res.raise_for_status()
    except Exception as exc :
        competitions.write(str(exc)+'\n')
    soup = bs4.BeautifulSoup(res.text,"lxml")
    # print(type(soup))
    



