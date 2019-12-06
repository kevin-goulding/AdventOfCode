filename = "...\\2015day2.txt"
infile = open(filename, 'r')
measList = []
for line in infile:
    measList.append(line)
infile.close()


def find2smallest(listof3nums):
    smallest2List = []
    smallest = min(listof3nums)
    smallest2List.append(smallest)
    listof3nums.remove(smallest)
    smallest = min(listof3nums)
    smallest2List.append(smallest)
    return (smallest2List)


def part1(measList):
    totalSqFt = 0
    for meas in measList:
        measSep = meas.split("x")
        h = int(measSep[0])
        l = int(measSep[1])
        w = int(measSep[2])
        surf1 = l*w
        surf2 = w*h
        surf3 = h*l
        smallest = min([surf1, surf2, surf3])
        sqFt = (2*surf1)+(2*surf2)+(2*surf3)+smallest
        totalSqFt += sqFt
    print(totalSqFt)

def part2(measList):
    totalRibbon = 0
    for meas in measList:
        measSep = meas.split("x")
        h = int(measSep[0])
        l = int(measSep[1])
        w = int(measSep[2])
        smallest2 = find2smallest([h,l,w])
        thisRibbon = (2*smallest2[0])+(2*smallest2[1])+(h*l*w)
        totalRibbon+= thisRibbon
    print(totalRibbon)

part1(measList)
part2(measList)