filename = "C:\\Users\\kevin\\Desktop\\2016day3\\input.txt" 
with open(filename) as f:
    inputList = f.readlines()
inputList = [x.strip() for x in inputList] 


counter = 0

for triangle in inputList:
    triangles = triangle.split()
    if (int(triangles[0])+int(triangles[1])>int(triangles[2])) and (int(triangles[1])+int(triangles[2])>int(triangles[0])) and (int(triangles[0])+int(triangles[2])>int(triangles[1])):
        counter += 1
print("Part 1:",counter)


counter2 = 0
group1start = 0
while group1start < len(inputList):
    row1 = inputList[group1start].split()
    row2 = inputList[group1start+1].split()
    row3 = inputList[group1start+2].split()
    if (int(row1[0])+int(row2[0])>int(row3[0])) and (int(row2[0])+int(row3[0])>int(row1[0])) and (int(row1[0])+int(row3[0])>int(row2[0])):
        counter2 += 1
    if (int(row1[1])+int(row2[1])>int(row3[1])) and (int(row2[1])+int(row3[1])>int(row1[1])) and (int(row1[1])+int(row3[1])>int(row2[1])):
        counter2 += 1
    if (int(row1[2])+int(row2[2])>int(row3[2])) and (int(row2[2])+int(row3[2])>int(row1[2])) and (int(row1[2])+int(row3[2])>int(row2[2])):
        counter2 += 1        
    group1start+=3

print("Part 2:",counter2)