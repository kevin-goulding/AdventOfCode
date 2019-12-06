filename = "C:\\Users\\kgoulding\\Desktop\\2015day3.txt"
infile = open(filename, 'r')
directionString = infile.readline()
infile.close()

def part1(directionString):
    x=0
    y=0
    coordDict={}
    coordDict[str(x)+"x"+str(y)]=1
    for direction in directionString:
        if direction == '^':
            y+=1
        elif direction == '>':
            x+=1
        elif direction == 'v':
            y-=1
        elif direction == "<":
            x-=1
        coordDict[str(x)+"x"+str(y)]=1
    print(len(coordDict.keys()))

def part2(directionString):
    x1=0
    y1=0
    x2=0
    y2=0
    coordDict={}
    coordDict[str(x1)+"x"+str(y1)]=1
    santa1MoveBool = True
    for direction in directionString:
        if direction == '^':
            if santa1MoveBool:
                y1+=1
            else:
                y2+=1
        elif direction == '>':
            if santa1MoveBool:
                x1+=1
            else:
                x2+=1
        elif direction == 'v':
            if santa1MoveBool:
                y1-=1
            else:
                y2-=1
        elif direction == "<":
            if santa1MoveBool:
                x1-=1
            else:
                x2-=1
        if santa1MoveBool:
            coordDict[str(x1)+"x"+str(y1)]=1
        else:
            coordDict[str(x2)+"x"+str(y2)]=1
        santa1MoveBool = not santa1MoveBool            
    print(len(coordDict.keys()))    

part1(directionString)
part2(directionString)


