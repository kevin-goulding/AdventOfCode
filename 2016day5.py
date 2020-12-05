import hashlib

puzzleString = 'ojvtpuvg'
testInt = 0
code = ""

while len(code)<8:
    testString = puzzleString + str(testInt)
    result = hashlib.md5(testString.encode())
    if result.hexdigest()[0:5]=='00000':
        code = code + result.hexdigest()[5]
    testInt += 1

puzzleString = 'ojvtpuvg'
testInt = 0
code2 = ["","","","","","","",""]
while "" in code2:
    testString = puzzleString + str(testInt)
    result = hashlib.md5(testString.encode())
    if result.hexdigest()[0:5]=='00000':
        try:
            existing = code2[int(result.hexdigest()[5])] 
            if code2[int(result.hexdigest()[5])] == "":
                code2[int(result.hexdigest()[5])] = result.hexdigest()[6]
                print(code2)
        except:
            pass

    testInt += 1

print("Part 1:",code)
print("Part 2:", "".join(code2))