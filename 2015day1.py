filename = "...\\2015day1.txt"
infile = open(filename, 'r')
text = infile.readline()
infile.close()

def part1(text):
    floor = 0
    for char in text:
        if char == "(":
            floor+=1
        elif char == ")":
            floor-=1
    print(floor)

def part2(text):
    posCounter = 0
    floor = 0
    for char in text:
        posCounter+=1
        if char == "(":
            floor+=1
        elif char == ")":
            floor-=1
        if floor == -1:
            print(posCounter)
            break

part1(text)
part2(text)