import hashlib

def part1(startString):
    go = True
    testInt = 0
    startString = 'iwrupvqb'
    while go:
        testString = startString+str(testInt)
        hashedstring = str((hashlib.md5(testString.encode())).hexdigest())
        if hashedstring[0:5]=='00000':
            print(testInt)
            break
        testInt+=1

def part2(startString):
    go = True
    testInt = 0
    startString = 'iwrupvqb'
    while go:
        testString = startString+str(testInt)
        hashedstring = str((hashlib.md5(testString.encode())).hexdigest())
        if hashedstring[0:6]=='000000':
            print(testInt)
            break
        testInt+=1

startString = 'iwrupvqb'
part1(startString)
part2(startString)