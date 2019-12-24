def part1(num):
    houses = []
    for house in range(int(num/10)):
        houses.append(10)
    correctHouses = []

    for elf in range(2,int(num/10)):
        thisHouse = elf
        while thisHouse < int(num/10):
            houses[thisHouse]+= elf*10
            if houses[thisHouse] >= num:
                correctHouses.append(thisHouse)
            thisHouse+= elf
    return(min(correctHouses))        

def part2(num):
    houses = []
    for house in range(int(num/10)):
        houses.append(11)
    correctHouses = []

    for elf in range(2,int(num/10)):
        thisHouse = elf
        deliveryCount = 0
        while thisHouse < int(num/10):
            houses[thisHouse]+= elf*11
            if houses[thisHouse] >= num:
                correctHouses.append(thisHouse)
            deliveryCount += 1
            if deliveryCount >= 50:
                break
            thisHouse+= elf
    return(min(correctHouses))        


print("Part 1:",part1(29000000))
print("Part 2:", part2(29000000))

