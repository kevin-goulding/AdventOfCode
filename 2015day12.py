filepath = "...\\2015day12.txt"

import json
with open(filepath) as json_file:
    data = json.load(json_file)

def walkJson(data, ignoreTerm = ""):
    totalNum = 0
    if 'dict' in str(type(data)):
        if ignoreTerm in list(data.values()):
            return(0)
        else:
            for entry in data:
                totalNum += walkJson(data[entry], ignoreTerm)
            return(totalNum)
    elif 'list' in str(type(data)):
        for listEntry in data:
            totalNum += walkJson(listEntry, ignoreTerm)
        return(totalNum)
    else:
        try:
            totalNum += int(data)
        except:
            pass
        return(totalNum)

print("Part 1: ",walkJson(data))
print("Part 2: ",walkJson(data, "red"))
