filename = "...\\2019day3.txt"
file = open(filename, 'r')
strings = []
for line in file:
    strings.append(line)
list0 = str.split(strings[0],',')
list1 = str.split(strings[1],',')
file.close()


def moveDirection(x,y,direction):
    if direction == "U":
        y += 1
    elif direction == "R":
        x += 1
    elif direction == "D":
        y -= 1
    elif direction == "L":
        x -= 1
    return(x,y)


def part1(list0,list1):
    x=0
    y=0
    matrixDict = {}
    matrixDict[str(x)+"x"+str(y)]=1
    for instruction in list0:
        direction = instruction[0]
        numSteps = int(instruction[1:])
        for stepCount in range(numSteps):
            x,y = moveDirection(x,y,direction)
            matrixDict[str(x)+"x"+str(y)]=1
    x=0
    y=0
    crossovers = []
    for instruction in list1:
        direction = instruction[0]
        numSteps = int(instruction[1:])
        for stepCount in range(numSteps):
            x,y = moveDirection(x,y,direction)
            entryString = str(x)+"x"+str(y)
            if entryString in matrixDict.keys():
                crossovers.append([x,y])

    #Establish first min value
    shortDist = abs(crossovers[0][0])+abs(crossovers[0][1])
    for crossover in crossovers:
        if abs(crossover[0])+abs(crossover[1])<shortDist:
            shortDist = abs(crossover[0])+abs(crossover[1])
    print(shortDist)


def part2(list0, list1):
    stepcounter = 0
    x=0
    y=0
    matrixDict = {}
    matrixDict[str(x)+"x"+str(y)]=stepcounter
    for instruction in list0:
        direction = instruction[0]
        numSteps = int(instruction[1:])
        for stepCount in range(numSteps):
            x,y = moveDirection(x,y,direction)
            stepcounter +=1
            matrixDict[str(x)+"x"+str(y)]=stepcounter
    stepcounter = 0
    x=0
    y=0
    crossovers = []
    for instruction in list1:
        direction = instruction[0]
        numSteps = int(instruction[1:])
        for stepCount in range(numSteps):
            x,y = moveDirection(x,y,direction)
            stepcounter +=1
            entryString = str(x)+"x"+str(y)
            if entryString in matrixDict.keys():
                crossovers.append([x,y,stepcounter, matrixDict[entryString]])
    #initialize first min value
    minSteps = crossovers[0][2]+crossovers[0][3]
    for crossover in crossovers:
        minStep = crossover[2]+crossover[3]
        if minStep < minSteps:
            minSteps = minStep
    print(minSteps)


part1(list0,list1)
part2(list0,list1)
