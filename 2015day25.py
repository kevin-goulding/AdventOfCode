#calculate how many times you do multiply, divide, remainder

def getToColumn(colNumber):
    col = 0
    colChange = 0
    for x in range(colNumber):
        colChange +=1
        col += colChange
    return(col)

def getSequenceNumber(colNumber, rowNumber):
    num = getToColumn(colNumber)
    rowChange = colNumber
    for x in range(rowNumber-1):
        num += rowChange
        rowChange +=1
    return(num)

def getCode(startVal, numIterations):
    val = startVal
    for x in range(numIterations-1):
        val = (val*252533)%33554393
    return(val)

print(getCode(20151125,getSequenceNumber(3083,2978)))