filepath = "...\\2019day1.txt"

massList = []
file = open(filepath, 'r')
for line in file:
    massList.append(int(line))
file.close()

def part1(massList):
    totalmass = 0
    for mass in massList:
        if mass>0:
            mass = (mass//3)-2
            totalmass += mass
    print(totalmass)


def part2(massList):
    totalmass = 0
    for mass in massList:
        while mass > 0:
            mass = (mass // 3) - 2
            if mass >0:
                totalmass += mass
    print(totalmass)


part1(massList)
part2(massList)