def FormatArr(strArr):
    for i in range(len(strArr)):
        strArr[i] = list(strArr[i])
    return strArr

def CheckPath(strArr):
    #print strArr
    print id(strArr)
    m = len(strArr)
    n = len(strArr[0])

    strArr[0][0] = '2'

    for i in range(1, n):
        if strArr[0][i] != '0':
            strArr[0][i] = strArr[0][i-1]

    for j in range(1, m):
        if strArr[j][0] != '0':
            strArr[j][0] = strArr[j-1][0]

    for i in range(1, m):
        for j in range(1, n):
            if strArr[i][j] != '0':
                strArr[i][j] = max(strArr[i][j-1], strArr[i-1][j])

    if strArr[m-1][n-1] == '2':
        return True
    # code goes here
    return False

def MatrixPath(strArr):
    print strArr
    if CheckPath(FormatArr(list(strArr))):
        return 'true'
    else:
        arr = FormatArr(list(strArr))
        count = 0
        print arr
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] == '0':
                    arr[i][j] == '1'
                    temp = [x[:] for x in arr]
                    if CheckPath(temp):
                        count += 1
        if count == 0:
            return 'not possible'
        else:
            return count
# keep this function call here


if __name__ == '__main__':
    i = ["10000", "11011", "10101", "11001"]
    print MatrixPath(i)
