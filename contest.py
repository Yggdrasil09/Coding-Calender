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
    else:
        res = requests.get(data[x])
    try:
        res.raise_for_status()
    except Exception as exc :
        competitions.write(str(exc)+'\n')
    soup = bs4.BeautifulSoup(res.text,"lxml")
    if x == 'Codechef':
        elements = soup.select(".dataTable")
        competitions.write("Present Contests : \n")
        # for element with present contests
        index = elements[0].select('tbody tr')
        for tags in index:
            td = tags.select("td")
            competitions.write('\nCompetion code : '+td[0].getText()+'\nContest Name: '+td[1].getText()+'\nStart time: '+td[2].getText()+'\nEnd time '+td[3].getText())
            competitions.write("\n--------------------------------------------------------------------------------------\n")
        competitions.write("Future Contests : \n")
        # for element with future contests
        index = elements[1].select('tbody tr')
        for tags in index:
            td = tags.select("td")
            competitions.write('\nCompetion code : '+td[0].getText()+'\nContest Name: '+td[1].getText()+'\nStart time: '+td[2].getText()+'\nEnd time '+td[3].getText())
            competitions.write("\n--------------------------------------------------------------------------------------\n")
    elif x == 'Codeforces':
        elements =soup.select('.datatable')
        competitions.write("Current or upcoming contests : \n")
        index = elements[0].select('tr[data-contestid]')
        for tags in index :
            td = tags.select("td")
            competitions.write('\nContest name : '+td[0].contents[0]+'\nStart time : '+ td[2].getText()+'\nDuration : '+td[3].getText())
            competitions.write("\n--------------------------------------------------------------------------------------\n")

competitions.close()


