def incrementPassword(currentPword):
    pwordList = []
    for char in currentPword:
        pwordList.append(char)
    pwordLength = len(pwordList)
    pointer = pwordLength-1
    go = True
    while go ==True:
        if pwordList[pointer] != 'z':
            pwordList[pointer] = chr(ord(pwordList[pointer])+1)
            go = False
        else:
            pwordList[pointer] = 'a'
            pointer -= 1
    newPword = ''.join(map(str, pwordList))     
    return newPword

def checkIncreasingThree(password):
    for x in range(len(password)-2):
        if password[x+1] == chr(ord(password[x])+1) and password[x+2] == chr(ord(password[x])+2):
            return(True)
    return(False)

def checkNoIOL(password):
    if 'i' in password or 'o' in password or 'l' in password:
        return(False)
    else:
        return(True)

def checkTwoPairs(password):
    pairCount = 0
    x =0
    while x < len(password)-1:
        if password[x] == password[x+1]:
            pairCount+=1
            x +=2
        else:
            x+=1
    if pairCount >= 2:
        return(True)
    else:
        return(False)

def findPassword(start):    
    password = incrementPassword(start)
    while not checkIncreasingThree(password) or not checkNoIOL(password) or not checkTwoPairs(password):
        password = incrementPassword(password)
    return(password)

password1 = findPassword('vzbxkghb')
password2 = findPassword(password1)

print("Part 1: ", password1)
print("Part 2: ", password2)

