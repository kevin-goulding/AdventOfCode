startRange = input("Enter start of range")
endRange = input("Enter end of range")

def checkAdjMatchPart1(numString):
    for x in range(len(numString)-1):
        if numString[x] == numString[(x+1)]:
            return True
    return False


def checkAdjMatchPart2(numString):
    for x in range(len(numString)-1):
        if numString[x] == numString[(x+1)]:
            try:
                if numString[x] != numString[(x+2)]:
                    if x > 0:
                        if numString[x] != numString[(x - 1)]:
                            return True
                    else:
                        return True
            except:
                if numString[x]==numString[(x-1)]:
                    return False
                else:
                    return True
    return False


def checkIncreasing(numString):
    for x in range(len(numString)):
        try:
            if int(numString[x])> int(numString[(x+1)]):
                return False
        except:
            return True



def part1(startRange, endRange):
    counter = 0
    dig0 = int(startRange[0])
    dig1 = int(startRange[1])
    dig2 = int(startRange[2])
    dig3 = int(startRange[3])
    dig4 = int(startRange[4])
    dig5 = int(startRange[5])

    for x in range(int(startRange), int(endRange)):
        numString = str(dig0)+str(dig1)+str(dig2)+str(dig3)+str(dig4)+str(dig5)
        if checkAdjMatchPart1(numString) and checkIncreasing(numString):
            counter+=1
        dig5+=1
        if dig5 >9:
            dig5 = 0
            dig4 +=1
            if dig4 > 9:
                dig4 = 0
                dig3 +=1
                if dig3 >9:
                    dig3=0
                    dig2+=1
                    if dig2 >9:
                        dig2 = 0
                        dig1+=1
                        if dig1 >9:
                            dig1 = 0
                            dig0+= 1
                            if dig0 >9:
                                break
    print(counter)

def part2(startRange, endRange):
    counter = 0
    dig0 = int(startRange[0])
    dig1 = int(startRange[1])
    dig2 = int(startRange[2])
    dig3 = int(startRange[3])
    dig4 = int(startRange[4])
    dig5 = int(startRange[5])

    for x in range(int(startRange), int(endRange)):
        numString = str(dig0)+str(dig1)+str(dig2)+str(dig3)+str(dig4)+str(dig5)
        if checkAdjMatchPart2(numString) and checkIncreasing(numString):
            counter+=1
        dig5+=1
        if dig5 >9:
            dig5 = 0
            dig4 +=1
            if dig4 > 9:
                dig4 = 0
                dig3 +=1
                if dig3 >9:
                    dig3=0
                    dig2+=1
                    if dig2 >9:
                        dig2 = 0
                        dig1+=1
                        if dig1 >9:
                            dig1 = 0
                            dig0+= 1
                            if dig0 >9:
                                break
    print(counter)


part1(startRange,endRange)
part2(startRange,endRange)