filepath = "...\\2019day8.txt"
file = open(filepath, 'r')
string = file.readline()
file.close()
layerDict = {}
increment = 150
pointer = 0
layerNum = 0
fewestZeroes = 150
answer = 0

for x in range(100):
    thisString = string[pointer:pointer+150]
    zeroCount = 0
    oneCount = 0
    twoCount = 0
    layerStringList = []
    for char in thisString:
        layerStringList.append(char)
        if char == '0':
            zeroCount+=1
        elif char =='1':
            oneCount+=1
        else:
            twoCount +=1
    if zeroCount < fewestZeroes:
        answer = oneCount * twoCount
        fewestZeroes = zeroCount
    layerDict[(layerNum)]=[zeroCount, oneCount, twoCount, layerStringList]
    layerNum+=1
    pointer+=150

finalStringList= []
for x in range(150):
    finalStringList.append('3')
currentLayer = 0
while '3' in finalStringList:
    layerContent = layerDict[currentLayer][3]
    for x in range(len(layerContent)):
        if layerContent[x]== '1' or layerContent[x]=='0':
            if finalStringList[x] == '3':
                finalStringList[x] = layerContent[x]
    currentLayer+=1

finalString = ""
for x in finalStringList:
    if x =='1':
        finalString+="*"
    else:
        finalString+=' '

print("Part1: ",answer)
print("Part2:")
print(finalString[0:25])
print(finalString[25:50])
print(finalString[50:75])
print(finalString[75:100])
print(finalString[100:125])
print(finalString[125:150])
