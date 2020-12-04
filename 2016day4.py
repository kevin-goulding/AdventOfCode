filename = "C:\\Users\\kevin\\Desktop\\2016day4\\input.txt" 
with open(filename) as f:
    inputList = f.readlines()
inputList = [x.strip() for x in inputList] 
alphabet = "abcdefghijklmnopqrstuvwxyz"
sums = 0
for entry in inputList:
    checksum = (entry[-6:-1])
    sectorID = int(entry[-10:-7])       
    letters = (entry[0:-10])

    charCountDict={}

    for char in letters:
        if char != "-":
            if char in charCountDict.keys():
                charCountDict[char]+=1
            else:
                charCountDict[char]=1

    testString = ""
    keys = (list(charCountDict.keys()))
    values = (list(charCountDict.values()))
    while len(testString) < len(checksum):
        maxVal = max(values)
        indices = [i for i, x in enumerate(values) if x == maxVal]
        tempString = ""
        for charLoc in indices:
            tempString = tempString + keys[charLoc]
            values[charLoc]=0
        sortedTemp = sorted(tempString)
        tempString = "".join(sortedTemp)
        testString = testString + tempString
    testString = testString[0:5]
    if testString == checksum:
        sums += sectorID
print("Part 1:",sums)
roomList = []

for entry in inputList:
    checksum = (entry[-6:-1])
    sectorID = int(entry[-10:-7])       
    letters = (entry[0:-11])
    decodedString = ""

    for char in letters:
        if char == "-":
            decodedString = decodedString+" "
        else:
            decodedString = decodedString + alphabet[((alphabet.index(char)+sectorID)%26)]
    if "north" in decodedString:
        print("Part 2:",sectorID)



   
        

