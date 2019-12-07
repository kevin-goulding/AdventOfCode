filepath = "...\\2015day8.txt"
file = open(filepath, 'r')
lineList = []
for line in file:
    lineList.append((line).strip())
file.close()

def evalCodeLength(string):
    hexadecimalChars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    length = 0
    pointer = 1
    while pointer < len(string)-1:

        if string[pointer] != "\\":
            length+=1
            pointer+=1
        else:
            if string[pointer+1]== "\\":
                length+=1
                pointer +=2
            elif string[pointer+1] =='"':
                if pointer == len(string)-2:
                    length+=1
                    pointer+=1
                else:
                    length+=1
                    pointer+=2
            elif string[pointer+1]=='x':
                try:
                    if string[pointer+2] in hexadecimalChars and string[pointer+3] in hexadecimalChars:
                        length+=1
                        pointer+=4
                    else:
                        length+=1
                        pointer+=1
                except:
                    length+=1
                    pointer+=1
            else:
                length+=1
                pointer+=1
    return(length)

def evalReprLength(string):
    length = 0
    pointer = 1
    while pointer < len(string):
        if string[pointer] != '\\' and string[pointer] != '\"':
            length+=1
            pointer+=1
        elif string[pointer] == '\\':
            length +=2
            pointer+=1
        elif string[pointer] == '\"':
            length+=2
            pointer+=1
    print(string)
    print(length+4)
    return(length+4)



reprTotal = 0
codeTotal = 0
machineTotal = 0
for line in lineList:
    machineTotal += len(line)
    codeTotal += evalCodeLength(line)
    reprTotal += evalReprLength(line)


print(machineTotal-codeTotal)
print(reprTotal-machineTotal)

