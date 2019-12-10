filepath = "...2015day14.txt"
file = open(filepath, 'r')
reindeerList = []
for line in file:
    reindeerList.append(line)
file.close()


def distanceTraveled(flyDist, flyTime, restTime, numSecs):
    flying = True
    totalDist = 0
    secPassed = 0
    timeFlying = 0
    while secPassed < numSecs:
        if flying == True:
            totalDist+=flyDist
            timeFlying += 1
            if timeFlying ==flyTime:
                flying = False
                timeFlying = 0
            secPassed +=1
        else:
            secPassed += restTime
            flying = True
    return(totalDist)

reindeerDict = {}
for line in reindeerList:
    key = line[:line.find('can ')-1]
    flyDist = int(line[line.find('fly')+4: line.find('km/s')-1])
    flyTime = int(line[line.find('km/s for')+9:line.find('seconds,')-1])
    restTime = int(line[line.find('rest for')+9: line.find('seconds.')-1])
    reindeerDict[key]=[flyDist,flyTime,restTime]


def part1():
    maxDist  = 0
    for reindeer in reindeerDict.keys():
        dist = distanceTraveled(reindeerDict[reindeer][0], reindeerDict[reindeer][1],reindeerDict[reindeer][2], 2503)
        if dist > maxDist:
            maxDist = dist
    return(maxDist)

def part2(raceSecs):
    reindeerPoints = {}
    for key in reindeerDict.keys():
        reindeerPoints[key] = 0
    for x in range(1,raceSecs+1):
        farthestTraveled = 0
        oneTimeDict = {}
        for reindeer in reindeerDict.keys():
            dist = distanceTraveled(reindeerDict[reindeer][0], reindeerDict[reindeer][1],reindeerDict[reindeer][2], x)
            oneTimeDict[reindeer] = dist
            if dist > farthestTraveled:
                farthestTraveled = dist
        for reindeer in oneTimeDict.keys():
            if oneTimeDict[reindeer] == farthestTraveled:
                reindeerPoints[reindeer]+=1            
    return(max(list(reindeerPoints.values())))
print("Part 1:",part1())   
print("Part2:",part2(2503))