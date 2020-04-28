for item in s:
        code = item['statecode']

        for o in data2:
            if o['statecode'] == code:
                item.update({'district': o['districtData']})
                actualdata.append(item)