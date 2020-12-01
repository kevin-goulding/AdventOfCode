filename = "C:\\Users\\kevin\\Desktop\\2016day1\\input.txt" 

with open(filename) as f:
    inputString = f.readline()

instructions = inputString.strip().split(", ")

x = 0
y = 0
direction = "N"

locations = []
locations.append((x,y))
hqLoc = "missing"
keepLooking = True

for instruction in instructions:
    dChange = instruction[0]
    distance = int(instruction[1:])

    if direction == "N":
        if dChange == "L":
            for d in range(distance):
                x -= 1
                if keepLooking == True:
                    coords = (x,y)
                    if coords in locations:
                        hqLoc = coords
                        keepLooking = False
                    else:
                        locations.append(coords)
            direction = "W"
        else:
            for d in range(distance):
                x += 1
                if keepLooking == True:
                    coords = (x,y)
                    if coords in locations:
                        hqLoc = coords
                        keepLooking = False
                    else:
                        locations.append(coords)
            direction = "E"

    elif direction == "E":
        if dChange == "L":
            for d in range(distance):
                y += 1
                if keepLooking == True:
                    coords = (x,y)
                    if coords in locations:
                        hqLoc = coords
                        keepLooking = False
                    else:
                        locations.append(coords)
            direction = "N"
        else:
            for d in range(distance):
                y -= 1
                if keepLooking == True:
                    coords = (x,y)
                    if coords in locations:
                        hqLoc = coords
                        keepLooking = False
                    else:
                        locations.append(coords)
            direction = "S"
  
    elif direction == "S":
        if dChange == "L":
            for d in range(distance):
                x += 1
                if keepLooking == True:
                    coords = (x,y)
                    if coords in locations:
                        hqLoc = coords
                        keepLooking = False
                    else:
                        locations.append(coords)
            direction = "E"
        else:
            for d in range(distance):
                x -= 1
                if keepLooking == True:
                    coords = (x,y)
                    if coords in locations:
                        hqLoc = coords
                        keepLooking = False
                    else:
                        locations.append(coords)
            direction = "W"

    elif direction == "W":
        if dChange == "L":
            for d in range(distance):
                y -= 1
                if keepLooking == True:
                    coords = (x,y)
                    if coords in locations:
                        hqLoc = coords
                        keepLooking = False
                    else:
                        locations.append(coords)
            direction = "S"
        else:
            for d in range(distance):
                y += 1
                if keepLooking == True:
                    coords = (x,y)
                    if coords in locations:
                        hqLoc = coords
                        keepLooking = False
                    else:
                        locations.append(coords)
            direction = "N"

print("Part 1: ",abs(x)+abs(y))
print("Part 2: ", (abs(hqLoc[0])+abs(hqLoc[1])))