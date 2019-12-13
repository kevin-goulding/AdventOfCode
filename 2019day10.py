filename = "c:\\Users\Kevin Goulding\\Desktop\\2019day10.txt"  #get rid of the opening
file  = open(filename, 'r')
astArray = []
for line in file:
    astArray.append(list(line.strip()))
file.close()

import math  

def calculateDistance(x1,y1,x2,y2):    #copied from carlundersman at https://community.esri.com/thread/158038
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return dist  
 
def getAngle(a, b, c): #copied from Manivannan Murugavel, posted at https://medium.com/@manivannan_data/find-the-angle-between-three-points-from-2d-using-python-348c513e2cd
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang

def getGCD(n, d):
        while d != 0:
            temp = d
            d = n%d
            n = temp
        return(n)

def getReducedSlope(x1,y1,x2,y2): 
    diffx1x2 = x2-x1
    diffy1y2 = y2-y1
    oldYPos = (diffy1y2>0)
    oldXPos = (diffx1x2>0)
    if diffx1x2 == 0:
        if oldYPos == True:
            diffy1y2 = 1
        else:
            diffy1y2=-1
    if diffy1y2 ==0:
        if oldXPos == True:
            diffx1x2 = 1
        else:
            diffx1x2 = -1
    else: 
        greatest=getGCD(diffy1y2, diffx1x2)
        diffy1y2 = int(diffy1y2/greatest)
        diffx1x2 = int(diffx1x2/greatest)
    if (oldYPos==True and diffy1y2 <0) or (oldYPos==False and diffy1y2 >0): 
        diffy1y2 = -diffy1y2
    if (oldXPos==True and diffx1x2 <0) or (oldXPos==False and diffx1x2 >0): 
        diffx1x2 = -diffx1x2
    return(diffx1x2, diffy1y2)


def part1(astArray):
    astLocList = []
    astBlockedCounts ={}
    for y in range(len(astArray)):
        for x in range(len(astArray[y])):
            if astArray[y][x] == "#":
                astLocList.append(str(x)+","+str(y))
                astBlockedCounts[str(x)+","+str(y)] = []
    astLocList = sorted(astLocList)
    for ast in astLocList:
        x1 = int(ast[:ast.find(',')])
        y1 = int(ast[ast.find(',')+1:])

        for otherAst in astLocList:
            if otherAst != ast:
                x2 = int(otherAst[:otherAst.find(',')])
                y2 = int(otherAst[otherAst.find(',')+1:])                       
                diffx1x2, diffy1y2 = getReducedSlope(x1,y1,x2,y2)
                testX = x2 + diffx1x2
                testY= y2 + diffy1y2

                while testX < len(astArray) and testX >=0 and testY < len(astArray) and testY >=0:
                    if (str(testX)+","+str(testY)) in astLocList:
                        if (str(testX)+","+str(testY)) not in astBlockedCounts[ast]:
                            astBlockedCounts[ast].append((str(testX)+","+str(testY)))
                    testX += diffx1x2
                    testY += diffy1y2
    mostSeen = 0  
    bestLoc = ""
    for key in astBlockedCounts.keys():
        numBlocked = len(astBlockedCounts[key])
        numCanSee = len(astLocList)-numBlocked-1
        if numCanSee > mostSeen:
            mostSeen = numCanSee
            bestLoc = key
    return(bestLoc, mostSeen)


def laser(astCoords, astArray):
    astList = []
    for y in range(len(astArray)):  
        for x in range(len(astArray[y])):
            if astArray[y][x] == "#":
                astList.append(str(x)+","+str(y))
    astList.remove(astCoords)

    angleDict = {}
    x1 = int(astCoords[:astCoords.find(',')])
    y1 = int(astCoords[astCoords.find(',')+1:])
    for entry in astList:
        x2 = int(entry[:entry.find(',')])
        y2 = int(entry[entry.find(',')+1:])
        angle = getAngle((x1,0), (x1,y1), (x2,y2))
        distance = calculateDistance(x1,y1,x2,y2)

        if angle in angleDict.keys():
            angleDict[angle][distance] = entry
        else:
            angleDict[angle]={distance:entry}
    shotNumber = 0
    shotDict = {}
    for key in (sorted(list(angleDict.keys()))):
        shotNumber+=1
        shotDict[shotNumber]= angleDict[key][min(list(angleDict[key].keys()))]
        del angleDict[key][min(list(angleDict[key].keys()))]
    return(shotDict)        

astLoc, numSeen = part1(astArray)
print("Part 1:", numSeen)
part2pair = ((laser(astLoc, astArray))[200])  
print("Part2: ",int(part2pair[:part2pair.find(',')])*100+int(part2pair[part2pair.find(',')+1:]))

