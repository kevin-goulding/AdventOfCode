filepath = "...2015day16.txt"
file = open(filepath, 'r')
lines = []
for line in file:
    lines.append(line)
file.close()

sueDict = {}
for line in lines:
    sueKey = line[:line.find(':')]
    sueDict[sueKey] = {}
    stuffList = line[line.find(':')+2:].split(', ')
    for thing in stuffList:
        sueDict[sueKey][thing[:thing.find(':')]]= int(thing[thing.find(':')+2:])

#sueList = list(sueDict.keys()).copy()

criteriaDict = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1,'vizslas':0}

def part1():
    for sue in sueDict.keys():
        thisSue = True
        for key in (sueDict[sue].keys()):
            if (sueDict[sue][key]) != criteriaDict[key]:
                thisSue = False
        if thisSue == True:
            print(sue)

def part2():
    for sue in sueDict.keys():
        thisSue = True
        for key in (sueDict[sue].keys()):
            if key == 'cats' or key == 'trees':
                if (sueDict[sue][key]<= criteriaDict[key]):
                    thisSue = False
            elif key == 'pomeranians' or key == 'goldfish':
                if (sueDict[sue][key]>= criteriaDict[key]):
                    thisSue = False
            else:    
                if (sueDict[sue][key]) != criteriaDict[key]:
                    thisSue = False
        if thisSue == True:
            print(sue)

part1()
part2()