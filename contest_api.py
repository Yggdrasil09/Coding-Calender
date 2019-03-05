import requests,json

response = requests.get("http://challengehuntapp.appspot.com/v2")
    

#writing to a file named competitions

competitions=open('competitions2.txt','w')

# print(response.status_code)

data = response.json()

#data is a list of contests

list1={
    'projecteuler.net':[],
    'hackerrank.com':[],
    'codechef.com':[],
    'hackerearth':[],
    'google.com/codejam':[],
    'codeforces.com':[],
    'codeforces.com/gyms':[],
    'kaggle.com':[],
    'topcoder':[],
    'facebook.com/hackercup':[]
}

list2={
    'projecteuler.net':[],
    'hackerrank.com':[],
    'codechef.com':[],
    'hackerearth':[],
    'google.com/codejam':[],
    'codeforces.com':[],
    'codeforces.com/gyms':[],
    'kaggle.com':[],
    'topcoder':[],
    'facebook.com/hackercup':[]
}

active = data['active']
pending = data["pending"]

for items in active:
    if items['host_name'] in list1:
        list1[items['host_name']].append(items)

for items in pending:
    if items['host_name'] in list2:
        list2[items['host_name']].append(items)

for contests in list1 :
    competitions.write('\n\n****\t'+contests+'\t****\n\n Active Contests')
    if(len(list1[contests])>0):
        for items in list1[contests]:
            competitions.write('\n\nContest name : '+items['contest_name']+'\nDuration : '+items['duration']+'\nEnd Time : '+items['end']+'\n')
            competitions.write("----------------------------------------------------------------------------------------")
    competitions.write('\n Pending Contests')
    if(len(list2[contests])>0):
        for items in list2[contests]:
            competitions.write('\n\nContest name : '+items['contest_name']+'\nDuration : '+items['duration']+'\nStart Time : '+items['start']+'\n')
            competitions.write("----------------------------------------------------------------------------------------")
