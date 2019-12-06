
#This was my first one after a long break from coding.... I don't like how I did this, but it works.

filepath = "...\\2019day5.txt"
file = open(filepath, 'r')
inputString = file.readline()
file.close()
inputList = inputString.split(',')
inputList = list(map(int, inputList))

def part1(inst):
    output = inst.copy()
    pointer=0
    go=True
    while go:
        instruction1 = output[pointer]
        if instruction1 == 1:
            output[output[(pointer + 3)]] = output[output[(pointer + 1)]] + output[output[(pointer + 2)]]
            pointer += 4
        elif instruction1 == 2:
            output[output[(pointer + 3)]] = output[output[(pointer + 1)]] * output[output[(pointer + 2)]]
            pointer +=4
        elif instruction1 == 3:
            num = int(input("Enter input code: "))
            output[output[(pointer+1)]] = num
            pointer+=2
        elif instruction1 == 4:
            print("Machine output: "+str(output[output[(pointer+1)]]))
            pointer+=2
        elif instruction1 == 99:
            break
        else:
            instString = str(instruction1)
            opcode = instString[(len(instString)-2):(len(instString))]
            modepos1 = '0'
            modepos2 = '0'
            modepos3 = '0'
            try:
                modepos1 = instString[-3]
            except:
                x=1
            try:
                modepos2 = instString[-4]
            except:
                x=2
            try:
                modepos3 = instString[-5]
            except:
                x=3

            if modepos1 == '0':
                num1 = output[output[(pointer+1)]]
            else:
                num1 = output[pointer+1]
            try:
                if modepos2 == '0':
                    num2 = output[output[(pointer+2)]]
                else:
                    num2 = output[pointer+2]
            except:
                pass
            if opcode == '01':
                outnum = num1+num2
                pointerAdd = 4
                if modepos3 =='0':
                    output[output[(pointer + 3)]] = outnum
                else:
                    output[pointer+3]=outnum

            elif opcode == '02':
                outnum = num1*num2
                pointerAdd = 4
                if modepos3 =='0':
                    output[output[(pointer + 3)]] = outnum
                else:
                    output[pointer+3]=outnum

            elif opcode == '03':
                outnum = int(input("Enter input code: "))
                pointerAdd = 2
            elif opcode == '04':
                print("Machine output: " + str(num1))
                pointerAdd = 2
            pointer+=pointerAdd


def part2(inst):
    output = inst.copy()
    pointer=0
    go=True
    while output[pointer]!= 99:
        pointerAdd = 0
        instruction = str(output[pointer])
        opcode = instruction[-1]
        modepos1 = '0'
        modepos2 = '0'

        try:
            modepos1 = instruction[-3]
        except:
            pass
        try:
            modepos2 = instruction[-4]
        except:
            pass

        if opcode == '1' or opcode == '2' or opcode == '7' or opcode == '8':
            param1 = output[pointer + 1]
            param2 = output[pointer + 2]
            param3 = output[pointer + 3]
            if modepos1 == '0':
                valnum1 = output[param1]
            else:
                valnum1 =  param1
            if modepos2 == '0':
                valnum2 = output[param2]
            else:
                valnum2 =  param2


            if opcode=='1':
                output[param3]=valnum1+valnum2
                pointerAdd = 4
            elif opcode == '2':
                output[param3]= valnum1*valnum2
                pointerAdd = 4
            elif opcode == '7':
                if valnum1<valnum2:
                    output[param3]=1
                else:
                    output[param3]=0
                pointerAdd = 4
            elif opcode == '8':
                if valnum1==valnum2:
                    output[param3]=1
                else:
                    output[param3]=0
                pointerAdd = 4


        elif opcode == '5' or opcode =='6':
            param1 = output[pointer + 1]
            param2 = output[pointer + 2]
            if modepos1 == '0':
                valnum1 = output[param1]
            else:
                valnum1 =  param1
            if modepos2 == '0':
                valnum2 = output[param2]
            else:
                valnum2 =  param2

            if opcode =='5':
                if valnum1 != 0:
                    pointer= valnum2
                    pointerAdd=0
                else:
                    pointerAdd = 3

            if opcode == '6':
                if valnum1 == 0:
                    pointer= valnum2
                    pointerAdd = 0
                else:
                    pointerAdd = 3

        elif opcode == '3' or opcode == '4':
            if opcode == '3':
                toWrite = int(input("Enter input: "))
                if modepos1 == '0':
                    output[output[pointer+1]] = toWrite
                else:
                    output[pointer+1]=toWrite

            if opcode == '4':
                if modepos1 == '0':
                    print("Machine printout opcode 4: "+str(output[output[pointer+1]]))
                else:
                    print("Machine printout opcode 4: "+str(output[pointer+1]))
            pointerAdd = 2

        pointer = pointer + pointerAdd

part1(inputList)
part2(inputList)
