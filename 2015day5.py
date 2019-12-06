filename = "...\\2015day5.txt"
infile = open(filename, 'r')
stringList = []
for line in infile:
    stringList.append(line)
infile.close()

def checkNice3Vowels(charString):
    vowels = 0
    for char in charString:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            vowels += 1
    if vowels > 2:
        return (True)
    else:
        return (False)

def checkNiceDuplicates(charString):
    for x in range(len(charString)-1):
        if charString[x]==charString[x+1]:
            return(True)
    return(False)

def checkNiceBadStrings(charString):
    for x in range(len(charString)-1):
        checkString = charString[x:(x+2)]
        if checkString=='ab' or checkString=='cd' or checkString=='pq' or checkString=='xy':
            return(False)
    return(True)


def checkNice2LettersTwice(charString):
    letterDict = {}
    for x in range(len(charString)-1):
        pair = charString[x:(x+2)]
        if pair in letterDict.keys():
            letterDict[pair]+=1
            try:
                if charString[x]==charString[(x-1)] and charString[x]==charString[(x+1)] and charString[x]!=charString[(x-2)]:
                    letterDict[pair] -= 1
            except:
                pass
        else:
            letterDict[pair]=1
    countList = (list(letterDict.values()))
    count2orMore = 0
    for entry in countList:
        if entry >= 2:
            count2orMore +=1
    if count2orMore>=1:
        return(True)
    else:
        return(False)

def checkNice1LetterRepeats(charString):
    for x in range(len(charString)-2):
        if charString[x]==charString[x+2]:
            return(True)
    return(False)


def part1(stringList):
    niceCounter = 0
    for string in stringList:
        if checkNice3Vowels(string) and checkNiceDuplicates(string) and checkNiceBadStrings(string):
            niceCounter+=1
    print(niceCounter)


def part2(stringList):
    niceCounter = 0
    for string in stringList:
        if checkNice2LettersTwice(string) and checkNice1LetterRepeats(string):
            niceCounter+=1
    print(niceCounter)


part1(stringList)
part2(stringList)