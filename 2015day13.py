from itertools import permutations
filename = "...\\2015day13.txt"
file = open(filename, 'r')
stringList =  []
for line in file:
    stringList.append(line)
file.close()

indivHapDict = {}
for line in stringList:
    name1 = line[:line.find('would')-1]
    name2 = line[line.find('next to')+8:line.find('.')]
    if 'lose' in line:
        sign = "-"
    else:
        sign = ""
    numString = line[line.find('would')+11:line.find('happiness')-1]
    sign += numString
    num = int(sign)
    if name1 not in indivHapDict.keys():
        indivHapDict[name1]= {name2:num}
    else:
        indivHapDict[name1][name2]=num

combHapDict = {}
for key in indivHapDict.keys():
    combHapDict[key]={}
for key in indivHapDict.keys():
    for entry in indivHapDict[key]:
        name1 = key
        name2 = entry
        combHapDict[name1][name2] = indivHapDict[name1][name2]+indivHapDict[name2][name1]
        combHapDict[name2][name1] = indivHapDict[name1][name2]+indivHapDict[name2][name1]
    
def eval(combHapDict):
    permList = (list(permutations(combHapDict.keys())))
    maxHappiness = 0
    for perm in permList:
        happiness = 0
        for x in range(len(perm)):
            try:
                happiness += combHapDict[perm[x]][perm[x+1]]
            except:
                happiness += combHapDict[perm[x]][perm[0]]
        if happiness > maxHappiness:
            maxHappiness = happiness
    return(maxHappiness)


combHapDict2 = combHapDict.copy()
oldPeople = combHapDict2.keys()
combHapDict2['You'] = {}
for person in oldPeople:
    combHapDict2[person]['You'] = 0
    combHapDict2['You'][person]=0

print("Part 1:", eval(combHapDict))
print("Part 2:", eval(combHapDict2))