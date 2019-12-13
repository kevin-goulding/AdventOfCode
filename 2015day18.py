filename="c:\\Users\\Kevin Goulding\\Desktop\\2015day18.txt"
file = open(filename, 'r')
oldArray = []
for line in file:
    oldArray.append(list(line.strip()))
file.close()

for y in range(len(oldArray)):
    j= [10 if x=='#' else 1 for x in oldArray[y]]
    oldArray[y] = j



def updateLights(oldArray):
    newArray = []
    totalCount = 0
    for y in range(len(oldArray)):
        newArray.append([])
        for x in range(len(oldArray[y])):
            count = 0
            c= oldArray[y][x]      #center
            if y != 0:
                count+= oldArray[y-1][x] #North
                if x< len(oldArray[y])-1:
                    count+= oldArray[y-1][x+1] #Northeast
                if x> 0: 
                    count+= oldArray[y-1][x-1]    #Northwest
            if x<len(oldArray[y])-1:
                count+= oldArray[y][x+1] #East
            if y < len(oldArray)-1:
                count+= oldArray[y+1][x] #south
                if x< len(oldArray[y])-1:
                    count+= oldArray[y+1][x+1] #Southeast
                if x>0:
                    count+= oldArray[y+1][x-1] #southwest
            if x > 0:
                count+= oldArray[y][x-1]   #west
            numAdjOn = count//10
            numAdjOff = count-(numAdjOn*10)
            if c ==10:
                if numAdjOn ==2 or numAdjOn ==3:
                    newArray[y].append(10)
                    totalCount +=1
                else:
                    newArray[y].append(1)
            else:
                if numAdjOn == 3:
                    newArray[y].append(10)
                    totalCount+=1
                else:
                    newArray[y].append(1)
    print(totalCount)
    return(newArray)

def updateLightsCornersOn(oldArray):
    newArray = []
    totalCount = 0
    for y in range(len(oldArray)):
        newArray.append([])
        for x in range(len(oldArray[y])):
            count = 0
            c= oldArray[y][x]      #center
            if y != 0:
                count+= oldArray[y-1][x] #North
                if x< len(oldArray[y])-1:
                    count+= oldArray[y-1][x+1] #Northeast
                if x> 0: 
                    count+= oldArray[y-1][x-1]    #Northwest
            if x<len(oldArray[y])-1:
                count+= oldArray[y][x+1] #East
            if y < len(oldArray)-1:
                count+= oldArray[y+1][x] #south
                if x< len(oldArray[y])-1:
                    count+= oldArray[y+1][x+1] #Southeast
                if x>0:
                    count+= oldArray[y+1][x-1] #southwest
            if x > 0:
                count+= oldArray[y][x-1]   #west
            numAdjOn = count//10
            numAdjOff = count-(numAdjOn*10)
            if c ==10:
                if numAdjOn ==2 or numAdjOn ==3:
                    newArray[y].append(10)
                    totalCount +=1
                else:
                    newArray[y].append(1)
            else:
                if numAdjOn == 3:
                    newArray[y].append(10)
                    totalCount+=1
                else:
                    newArray[y].append(1)
    if newArray[0][0] ==1:
        newArray[0][0] =10
        totalCount+=1
    if newArray[0][len(newArray)-1] ==1:
        newArray[0][len(newArray)-1] =10
        totalCount+=1
    if newArray[len(newArray)-1][0] ==1:
        newArray[len(newArray)-1][0] =10
        totalCount+=1
    if newArray[len(newArray)-1][len(newArray)-1] ==1:
        newArray[len(newArray)-1][len(newArray)-1] =10
        totalCount+=1 

    print(totalCount)
    return(newArray)



for x in range(100):
    oldArray = updateLightsCornersOn(oldArray)




