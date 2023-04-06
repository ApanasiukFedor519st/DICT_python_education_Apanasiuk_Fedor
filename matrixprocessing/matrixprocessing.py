def matrixenter():
    print("Enter the size")
    inp = input().split()
    row = int(inp[0])
    colums = int(inp[1])
    listA = []

    print("Enter the matrix")
    while row > 0:
        inp = input().split()[:colums]
        listA.append(list(map(int,inp)))
        row = row - 1
    return listA

def matrixprint(matrix):
    for i in range(0,len(matrix)):
        for k in range(0,len(matrix[0])):
            print(matrix[i][k], end=" ")
        print()

def matrixadd():
    a = matrixenter()
    b = matrixenter()
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        for i in range(0, len(a)):
            for k in range(0, len(a[0])):
                a[i][k] += b[i][k]
        matrixprint(a)
    else:
        print("ERROR")

def matrixconst():
    a = matrixenter()
    print("Write a constant")
    c = int(input())
    for i in range(0, len(a)):
        for k in range(0, len(a[0])):
            a[i][k] *= c
    matrixprint(a)

def matrixmultiplymatrix():
    a = matrixenter()
    b = matrixenter()
    if len(a[0]) != len(b):
        print("ERROR")
    else:
        matrix = [[0 for j in range(len(b[0]))] for i in range(len(a))]
        for i in range(0, len(a)):
            for j in range(0, len(b[i])):
                result = 0
                for k in range(0, len(b)):
                    result += a[i][k] * b[k][j]
                matrix[i][j] = int(result) if round(result) == 0 else result
        matrixprint(matrix)
matrixmultiplymatrix()