import requests,json

response = requests.get("https://clist.by:443/api/v1/contest/?username=Karthikp99&api_key=54330957009d28b8a24eb8b7cb48dde28ae402da")

data = response.json()

data =data["objects"]

