filename = "...\\2019day6.txt"
infile = open(filename, 'r')
orbits = []
for line in infile:
    orbits.append(line)
infile.close()

#orbitDict is a dictionary where key:value = (orbiter): (planet that orbiter orbits)
orbitDict = {}
for orbit in orbits:
    twoOrbitList = orbit.split(")")
    orbitDict[twoOrbitList[1][0:3]]=twoOrbitList[0][0:3]


def pursueorbit(key, orbitCount): 
    orbitCount+=1
    if orbitDict[key]=='COM':
        return(orbitCount)
    else:
        return(pursueorbit(orbitDict[key], orbitCount))


def numToPlanets(orbiter, orbitDict):
    posDict = {}
    position = 1
    orbited = orbitDict[orbiter]
    while orbited != 'COM':
        posDict[orbited] = position
        position += 1
        orbiter = orbited
        orbited = orbitDict[orbiter]
    return (posDict)


def part1(orbitDict):
    totalOrbits=0
    for key in orbitDict.keys():
        totalOrbits += pursueorbit(key, 0)
    print(totalOrbits)

def part2(orbitDict):
    santa = numToPlanets('SAN', orbitDict)
    you = numToPlanets('YOU', orbitDict)
    common = []
    for key in santa.keys():
        if key in you.keys():
            totalDist = santa[key]+you[key]
            common.append(totalDist)
    print(min(common)-2)  #Subtract 2 to account for the fact that we're looking at the distance between planets that SAN and YOU orbit. Without subtracting 2, it includes a move from SAN to its planet, and YOU to its planet


part1(orbitDict)
part2(orbitDict)