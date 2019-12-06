filepath = "...\\2015day6.txt"
directionStrings = []
file = open(filepath, 'r')
for line in file:
    directionStrings.append(line)
file.close()

def createStartArray(width,height,baseEntry):
    lightArray = []
    for x in range(width):
        lightArray.append([])
        for y in range(height):
            lightArray[x].append(baseEntry)
    return(lightArray)

def breakownDirection(direction):
    throughStart = direction.find('through')
    secondSetStart = throughStart+8
    secondSetString = direction[secondSetStart:len(direction)]
    set2list = secondSetString.split(',')
    set2x = set2list[0]
    set2y = set2list[1]
    toggle = False
    turnon = False
    turnoff = False
    if direction.find('toggle')>-1:
        firstSetStart = 7
        toggle = True
    elif direction.find('on')>-1:
        firstSetStart = 8
        turnon = True
    elif direction.find('off')>-1:
        firstSetStart = 9
        turnoff = True
    firstSetString = direction[firstSetStart:throughStart - 1]
    set1list = firstSetString.split(',')
    set1x = set1list[0]
    set1y = set1list[1]
    return(set1x,set1y,set2x,set2y,toggle,turnon,turnoff)

def part1(directionStrings):
    lightArray = createStartArray(1000,1000,False)
    for direction in directionStrings:
        set1x, set1y, set2x, set2y, toggle, turnon, turnoff = breakownDirection(direction)
        for x in range(int(set1x),int(set2x)+1):
            for y in range(int(set1y),int(set2y)+1):
                if toggle:
                    lightArray[x][y]=not lightArray[x][y]
                if turnon:
                    lightArray[x][y] = True
                if turnoff:
                    lightArray[x][y] = False
    lightCounter = 0
    for x in lightArray:
        for y in x:
            if y == True:
                lightCounter +=1
    print(lightCounter)

def part2(directionStrings):
    lightArray = createStartArray(1000,1000,0)
    for direction in directionStrings:
        set1x, set1y, set2x, set2y, toggle, turnon, turnoff = breakownDirection(direction)
        for x in range(int(set1x),int(set2x)+1):
            for y in range(int(set1y),int(set2y)+1):
                if toggle:
                    lightArray[x][y]+=2
                if turnon:
                    lightArray[x][y]+=1
                if turnoff:
                    if lightArray[x][y] >0:
                        lightArray[x][y]-=1
    lightCounter = 0
    for x in lightArray:
        for y in x:
                lightCounter += y
    print(lightCounter)

part1(directionStrings)
part2(directionStrings)