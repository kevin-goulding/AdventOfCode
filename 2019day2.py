filepath = "...\\2019day2.txt"
file = open(filepath, 'r')
input = (file.readline()).split(',')
file.close()
input= list(map(int, input))

def part1(input, replacement1, replacement2):
    output = input.copy()
    output[1] = replacement1
    output[2] = replacement2
    x = 0
    while output[x] != 99:
        if output[x] ==1:
            output[output[(x+3)]]= output[output[(x+1)]]+output[output[(x+2)]]
        elif output[x] ==2:
            output[output[(x + 3)]] = output[output[(x + 1)]] * output[output[(x + 2)]]
        else:
                print("UHOH")
        x+=4
    print(output[0])


def part2(input, goal):
    for noun in range(100):
        for verb in range(100):
            output = input.copy()
            output[1]=noun
            output[2]=verb
            for x in range(len(output)):
                if x%4 ==0:
                    if output[x] ==1:
                        output[output[(x+3)]]= output[output[(x+1)]]+output[output[(x+2)]]
                    elif output[x] ==2:
                        output[output[(x + 3)]] = output[output[(x + 1)]] * output[output[(x + 2)]]
                    elif output[x] == 99:
                        if output[0]==goal:
                            print(str(100*noun+verb))
                        break
                    else:
                        print("UHOH")


#For part 1, 12 and 2 were provided in my instructions as arguments
#For part 2, 19690720 was provided in my instructions as an argument

part1(input, 12, 2)
part2(input, 19690720)
