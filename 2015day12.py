filepath = "c:\\Users\\Kevin Goulding\\Desktop\\2015day12.txt"
file = open(filepath, 'r')
text = file.readline()
file.close()

import json
with open(filepath) as json_file:
    data = json.load(json_file)


def walkJson(data):
    totalNum = 0
    if 'dict' in str(type(data)):
        for entry in data:
            totalNum += walkJson(data[entry])
        return(totalNum)
    elif 'list' in str(type(data)):
        for listEntry in data:
            totalNum += walkJson(listEntry)
        return(totalNum)
    else:
        try:
            totalNum += int(data)
            return(totalNum)
        except:
            return(totalNum)

def walkJsonIgnoreRed(data):
    totalNum = 0
    if 'dict' in str(type(data)):
        if "red" in list(data.values()):
            return(0)
        else:
            for entry in data:
                totalNum += walkJsonIgnoreRed(data[entry])
            return(totalNum)
    elif 'list' in str(type(data)):
        for listEntry in data:
            totalNum += walkJsonIgnoreRed(listEntry)
        return(totalNum)
    else:
        try:
            totalNum += int(data)
            return(totalNum)
        except:
            return(totalNum)

print("Part 1: ",walkJson(data))
print("Part 2: ",walkJsonIgnoreRed(data))
