filepath = "c:\\Users\\Kevin Goulding\\Desktop\\2015day15.txt"
file = open(filepath, 'r')
fileLines = []
for line in file:
    fileLines.append(line)
file.close()

ingredients = {}
for line in fileLines:
    ingredient = line[:line.find(':')]
    capacity = int(line[line.find('capacity')+9:line.find('durability')-2])
    durability = int(line[line.find('durability')+11:line.find('flavor')-2])
    flavor = int(line[line.find('flavor')+7:line.find('texture')-2])
    texture = int(line[line.find('texture')+8:line.find('calories')-2])
    calories = int(line[line.find('calories')+9:])
    ingredients[ingredient] = {'capacity':capacity, 'durability':durability, "flavor":flavor, "texture":texture, "calories":calories}

def getScore(numTspSugar, numTspSprinkles, numTspCandy, numTspChocolate):
    capacity = numTspSugar*3 + numTspSprinkles*-3 + numTspCandy*-1 + numTspChocolate*0
    if capacity <0:
        return(0)
    durability = numTspSugar*0 + numTspSprinkles*3 + numTspCandy*0 + numTspChocolate*0
    if durability <0:
        return(0)
    flavor = numTspSugar*0 + numTspSprinkles*0 + numTspCandy*4 + numTspChocolate*-2
    if flavor <0:
        return(0)
    texture = numTspSugar*-3 + numTspSprinkles*0 + numTspCandy*0 + numTspChocolate*2
    if texture <0:
        return(0)
    return(capacity*durability*flavor*texture)

def numCal(numTspSugar, numTspSprinkles, numTspCandy, numTspChocolate):
    calories = numTspSugar*2 + numTspSprinkles*9 + numTspCandy + numTspChocolate*8
    return(calories)

maxScore1 = 0
for numTspSugar in range(100):        
    for numTspSprinkles in range(100-numTspSugar):        
        for numTspCandy in range(100-(numTspSugar +numTspSprinkles)):       
            numTspChocolate = 100-(numTspSugar +numTspSprinkles+numTspCandy)
            thisScore = getScore(numTspSugar, numTspSprinkles, numTspCandy, numTspChocolate)
            if thisScore > maxScore1:
                maxScore1 = thisScore


maxScore2 = 0
for numTspSugar in range(100):        
    for numTspSprinkles in range(100-numTspSugar):        
        for numTspCandy in range(100-(numTspSugar +numTspSprinkles)):       
            numTspChocolate = 100-(numTspSugar +numTspSprinkles+numTspCandy)
            if numCal(numTspSugar, numTspSprinkles, numTspCandy, numTspChocolate) ==500:
                thisScore = getScore(numTspSugar, numTspSprinkles, numTspCandy, numTspChocolate)
                if thisScore > maxScore2:
                    maxScore2 = thisScore


print("Part 1:", maxScore1)
print("Part 2:", maxScore2)




