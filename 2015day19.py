filename = "...\\2015day19.txt"  
file  = open(filename, 'r')
molReplacements = {}
moleculeSizeDict = {}
longtoShortDict = {}
codeString = ''
for line in file:
    if line.find('=>') != -1:
        key = line[:line.find('=>')-1]
        conversion = line[line.find('=>')+3:].strip()
        numAtoms = sum(1 for c in conversion if c.isupper())
        if numAtoms in moleculeSizeDict:
            moleculeSizeDict[numAtoms].append(conversion)
        else:
            moleculeSizeDict[numAtoms] = [conversion]

        longtoShortDict[conversion] = key

        if key in molReplacements:
            molReplacements[key].append(conversion)
        else:
            molReplacements[key] = [conversion]
    else:
        if len(line.strip())!=0:
            codeString = line.strip()

file.close()


def part1(codeString, molReplacements):
    combList = []
    start = 0
    while start <len(codeString):
        try:
            char = codeString[start:start+2]
            if char[1].isupper():
                char = codeString[start]
                advance = 1
            else:
                advance = 2
        except:
            char = codeString[start]
            advance = 1

        if char in molReplacements:
            for replacement in molReplacements[char]:
                oldString = codeString
                firstHalf = oldString[:start]
                secondHalf = oldString[start+advance:]       
                newString = firstHalf+replacement+secondHalf

                if newString not in combList:
                    combList.append(newString)
        start+=advance
    return(combList)

print("Part 1:", len(part1(codeString, molReplacements)))

upperCount = 0
for character in codeString:
    if character.isupper():
        upperCount +=1


def findall(p, s):
    counter = 0
    i = s.find(p)
    while i != -1:
        counter +=1
        i = s.find(p, i+1)
    return(counter)

print("Part 2:", upperCount-(findall('Rn',codeString))-(findall('Ar',codeString))-2*(findall('Y',codeString))-1)