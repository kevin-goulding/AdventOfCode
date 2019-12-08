def LookAndSay(num):
    oldString = str(num)
    newString = ""
    go = True
    pointer = 0
    while go:
        currentChar  = oldString[pointer]
        same = True
        counter = 1
        while same == True:
            try:
                nextChar = oldString[pointer+counter]
                if nextChar != currentChar:
                    same = False
                    pointer+=counter
                else:
                    counter +=1
            except:
                same = False
                go = False
        newString += str(counter) +str(currentChar)
    return(newString)

def eval(string, num):
    first = LookAndSay(string)
    for x in range(num-1):
        first = LookAndSay(first)
    return(len(first))

print("Part 1: "+str(eval(1113122113,40)))
print("Part 2: "+str(eval(1113122113,50)))


