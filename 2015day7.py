filename = "...\\2015day7.txt"
infile = open(filename, 'r')
instructionBook = []
for line in infile:
    instructionBook.append(line)
infile.close()

def binString(number):
    number = int(number)
    return(bin(number)[2:].zfill(16))

def binAnd(binstring1, binstring2):
    returnString = ""
    for x in range(len(binstring1)):
        if binstring1[x] =='1' and binstring2[x] =='1':
            returnString += "1"
        else:
            returnString +="0"
    return(returnString)

def binOr(binstring1, binstring2):
    returnString = ""
    for x in range(len(binstring1)):
        if binstring1[x] =='1' or binstring2[x] =='1':
            returnString += "1"
        else:
            returnString +="0"
    return(returnString)

def binNot(binstring):
    returnString = ""
    for x in range(len(binstring)):
        if binstring[x] =='1':
            returnString += "0"
        else:
            returnString +="1"
    return(returnString)

def binLShift(binstring, num):
    returnString = ""
    for x in range(16):
        try:      
            returnString += binstring[num+x]
        except:
            returnString += '0'
    return(returnString)

def binRShift(binstring, num):
    returnString = binstring[:-num].zfill(16)
    return(returnString)



instructionDict = {}
for instruction in instructionBook:
    key = instruction[instruction.find('->')+3:].strip()
    param1 = None
    param2 = None
    value = None

    if instruction.find('AND')>-1:
        operator = 'AND'
        param1 = instruction[:(instruction.find('AND')-1)].strip()
        param2 = instruction[instruction.find('AND')+4:instruction.find('->')-1]
    elif instruction.find('OR')>-1:
        operator = 'OR'
        param1 = instruction[:(instruction.find('OR')-1)].strip()
        param2 = instruction[instruction.find('OR')+3:instruction.find('->')-1]
    elif instruction.find('NOT') > -1:
        operator = 'NOT'
        param1 =  instruction[4:instruction.find('->')-1]

    elif instruction.find('RSHIFT') > -1:
        operator = 'RSHIFT'
        param1 = instruction[:(instruction.find('RSHIFT')-1)]
        value = int(instruction[(instruction.find('RSHIFT')+7):instruction.find('->')-1])

    elif instruction.find('LSHIFT') > -1:
        operator = 'LSHIFT'
        param1 = instruction[:(instruction.find('LSHIFT')-1)]
        value = int(instruction[(instruction.find('LSHIFT')+7):instruction.find('->')-1])

    else:
        operator = 'ASSIGN'
        param = instruction[:instruction.find('->')-1]
        try:
            value = int(param)
        except:
            param1 = param

    instructionDict[key] = [operator, param1, param2, value]

evaluationDict = {}

def evaluate(dictEntry):
    if dictEntry in evaluationDict:
        return(evaluationDict[dictEntry])
    else:
        value = ''
        if instructionDict[dictEntry][0] =='AND':
            if instructionDict[dictEntry][1]=='1':
                value = binAnd(binString(1),(evaluate(instructionDict[dictEntry][2])))
            else:
                value = binAnd((evaluate(instructionDict[dictEntry][1])), (evaluate(instructionDict[dictEntry][2])))
        elif instructionDict[dictEntry][0] =='OR':
            value = binOr((evaluate(instructionDict[dictEntry][1])), (evaluate(instructionDict[dictEntry][2])))
        elif instructionDict[dictEntry][0] == 'NOT':
            value = binNot((evaluate(instructionDict[dictEntry][1])))
        elif instructionDict[dictEntry][0] == 'RSHIFT':
            value = binRShift((evaluate(instructionDict[dictEntry][1])),instructionDict[dictEntry][3])
        elif instructionDict[dictEntry][0] == 'LSHIFT':
            value = binLShift((evaluate(instructionDict[dictEntry][1])),instructionDict[dictEntry][3])
        elif instructionDict[dictEntry][0] == 'ASSIGN':
            if instructionDict[dictEntry][3] is not None:
                value = binString(instructionDict[dictEntry][3])
            else:
                value = (evaluate(instructionDict[dictEntry][1]))
        evaluationDict[dictEntry] = value
        return(value)

def part1():
    evaluationDict.clear()
    print(int(evaluate('a'),2))

def part2():
    evaluationDict.clear()
    evaluationDict['b'] = (binString(16076))
    print(int(evaluate('a'),2))

part1()
part2()
