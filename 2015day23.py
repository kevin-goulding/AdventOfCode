def processLine(line):
    code = line[0:3]
    if code != 'jmp':
        register = line[4]
        if code == 'jie' or code =='jio':
            offset = int(line[line.find(',')+2:])
        else:
            offset = None
    else:
        register = None
        offset = int(line[4:])
    return([code, register, offset])

instructions = []
filename = "...\\2015day23.txt"
infile = open(filename, 'r')
for line in infile:
    instructions.append(processLine(line.strip()))

def runInstructions(startValA):
    a = startValA
    b = 0
    instructionCode = 0
    while instructionCode < len(instructions):
        code = instructions[instructionCode][0]
        register = instructions[instructionCode][1]
        offset = instructions[instructionCode][2]
        if code =='inc':
            if register == 'a':
                a+=1
            else:
                b+=1
            instructionCode +=1
        elif code == 'hlf':
            if register == 'a':
                a = a/2
            else:
                b = b/2
            instructionCode +=1
        elif code == 'tpl':
            if register == 'a':
                a = a*3
            else:
                b = b*3
            instructionCode +=1
        elif code == 'jmp':
            instructionCode = instructionCode + offset
        elif code == 'jie':
            if register == 'a':
                if a % 2 == 0:
                    instructionCode = instructionCode + offset   
                else:
                    instructionCode += 1
            elif register == 'b':
                if b % 2==0:
                    instructionCode = instructionCode+offset
                else:
                    instructionCode +=1     

        elif code == 'jio':
            if register == 'a':
                if a ==1:
                    instructionCode = instructionCode + offset   
                else:
                    instructionCode += 1
            elif register == 'b':
                if b ==1:
                    instructionCode = instructionCode+offset
                else:
                    instructionCode +=1     
    return(b)

print("Part 1:",runInstructions(0))
print("Part 2:",runInstructions(1))   