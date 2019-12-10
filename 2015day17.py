filepath = "...2015day17.txt"
file = open(filepath, 'r')
containers = []
for line in file:
    containers.append(int(line.strip()))
file.close()

def numCombs(containers, runningTotal, goal):
    count = 0
    x= 0
    for entry in containers:
        x+=1
        if entry + runningTotal == goal:
            count += 1
        elif entry + runningTotal > goal:
            pass
        else:
            newContainers = containers[x:len(containers)]
            newRunningTotal = entry + runningTotal
            count += numCombs(newContainers, newRunningTotal, goal)
    return(count)


def combLists(containers, runningTotal, goal, depth):
    depth+=1
    count = 0
    x= 0
    rlist = []
    for entry in containers:
        x+=1
        if entry + runningTotal == goal:
            rlist.append(depth)
        elif entry + runningTotal > goal:
            pass
        else:
            newContainers = containers[x:len(containers)]
            newRunningTotal = entry + runningTotal
            toAdd = (combLists(newContainers, newRunningTotal, goal, depth))
            if toAdd !=[]:
                rlist.append(toAdd)
    return(rlist)


print("Part 1:",numCombs(containers,0,150))

listString = (str(combLists(containers, 0, 150, 0)))
numDict = {}
for char in listString:
    try:
        if int(char) in numDict.keys():
            numDict[int(char)]+=1
        else:
            numDict[int(char)] = 1
    except:
        pass
print("Part 2:",numDict[min(list(numDict.keys()))])



