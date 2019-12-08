from itertools import permutations

filepath = 'c:\\Users\\Kevin Goulding\\Desktop\\2015day9.txt'
file = open(filepath, 'r')
distanceList = []
for line in file:
    distanceList.append(line)
countryList = []
countryDict = {}
for distance in distanceList:
    country1 = distance[:distance.find(" ")]
    country2 = distance[distance.find('to ')+3:distance.find('=')-1]
    distance = int(distance[distance.find('=')+2:])
    if country1 not in countryDict.keys():
        countryDict[country1] = {country2:distance}
    else:
        countryDict[country1][country2] = distance
    if country2 not in countryDict.keys():
        countryDict[country2] = {country1:distance}
    else:
        countryDict[country2][country1] = distance

def part1():
    shortestDist = 9999999999
    for perm in (list(permutations(list(countryDict.keys())))):
        totalDist = 0
        for x in range(len(perm)-1):
            totalDist += countryDict[perm[x]][perm[x+1]]
        if totalDist < shortestDist:
            shortestDist = totalDist
    print(shortestDist)

def part2():
    longestDist = 0
    for perm in (list(permutations(list(countryDict.keys())))):
        totalDist = 0
        for x in range(len(perm)-1):
            totalDist += countryDict[perm[x]][perm[x+1]]
        if totalDist > longestDist:
            longestDist = totalDist
    print(longestDist)

part1()
part2()