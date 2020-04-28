total=requests.get('https://api.covid19api.com/summary')
s=total.text
data=json.loads(s)
Total=data['Global']['TotalConfirmed']
new_case=data['Global']['NewConfirmed']
Total_death=data['Global']['TotalDeaths']

req = requests.get('https://api.covid19india.org/data.json')
data1 = req.json()
s=data1['statewise']
allind=data1['statewise'][0]
req2 = requests.get('https://api.covid19india.org/v2/state_district_wise.json')
data2 = req2.json()
actualdata = []
for item in s:
    code = item['statecode']

    for o in data2:
        if o['statecode'] == code:
            item.update({'district': o['districtData']})
            actualdata.append(item)