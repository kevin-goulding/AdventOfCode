filename = "C:\\Users\\kevin\\Desktop\\2016day2\\input.txt" 
with open(filename) as f:
    inputList = f.readlines()
inputList = [x.strip() for x in inputList] 

dictP1 = {"-1,1":"1", "0,1":"2","1,1":"3", "-1,0":"4", "0,0":"5", "1,0":"6", "-1,-1":"7", "0,-1":"8", "1,-1":"9"}
dictP2 = {"0,2":"1", "-1,1":"2", "0,1":"3", "1,1":"4", "-2,0":"5", "-1,0":"6", "0,0":"7", "1,0":"8", "2,0":"9", "-1,-1":"A", "0,-1":"B", "1,-1":"C", "0,-2":"D"}

def moveP1(direction, oldX, oldY):
    if direction == "U":
        return(oldX,min((oldY+1),1))
    elif direction == "R":
        return(min((oldX+1),1),oldY)  
    elif direction == "D":
        return(oldX,max((oldY-1),-1))
    elif direction == "L":
        return(max((oldX-1),-1),oldY)  

finalString1 = ""
x,y = 0,0

for entry in inputList:
    for character in entry:
        x,y = moveP1(character,x,y)
    finalString1 = finalString1 + dictP1[str(x)+","+str(y)]
    x,y = 0,0

print("Part 1: " +finalString1)

def moveP2(direction, oldX, oldY):
    if direction == "U":
        if oldY == -2 or oldY ==-1:
            return(oldX, (oldY+1))
        elif oldY == 0 and abs(oldX)<2:
            return(oldX, oldY+1)
        elif oldY == 1 and oldX ==0:
            return(oldX, oldY+1)
        else:
            return(oldX, oldY)

    elif direction == "D":
        if oldY == 2 or oldY ==1:
            return(oldX, oldY-1)
        elif oldY == 0 and abs(oldX)<2:
            return(oldX, oldY-1)
        elif oldY == -1 and oldX == 0:
            return(oldX, oldY-1)
        else:
            return(oldX,oldY)

    elif direction == "R":
        if oldX == -2 or oldX ==-1:
            return(oldX+1, (oldY))
        elif oldX == 0 and abs(oldY)<2:
            return(oldX+1, oldY)
        elif oldX == 1 and oldY ==0:
            return(oldX+1, oldY)
        else:
            return(oldX, oldY)

    elif direction == "L":
        if oldX == 2 or oldX ==1:
            return(oldX-1, oldY)
        elif oldX == 0 and abs(oldY)<2:
            return(oldX-1, oldY)
        elif oldX == -1 and oldY == 0:
            return(oldX-1, oldY)
        else:
            return(oldX,oldY)

finalString2 = ""
x = 0
y = 0

for entry in inputList:
    for character in entry:
        x,y = moveP2(character,x,y)
    finalString2 = finalString2 + dictP2[str(x)+","+str(y)]
    x = 0
    y = 0

print("Part 2: "+finalString2)