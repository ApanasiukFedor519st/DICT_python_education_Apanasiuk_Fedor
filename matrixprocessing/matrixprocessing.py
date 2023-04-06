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

def mainmenu():
    while True:
        choice = int(input('''1. Add matrices 
2. Multiply matrix by a constant 
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant 
0. Exit 
'''))
        if choice == 0: return None
        elif choice == 1: matrixadd()
        elif choice == 2: matrixconst()
        elif choice == 3: matrixmultiplymatrix()
        elif choice == 4:
            key = 0
            while key < 1 or key > 4:
                key = int(input('''1. Main diagonal 
2. Side diagonal 
3. Vertical line 
4. Horizontal line \n'''))
            matrix = matrixenter()
            matrixtranspose(matrix,key)
        elif choice == 5:
            matrix = matrixenter()
            print(determinant(matrix))

def matrixtranspose(matrix_1,k):
    result_matrix = []
    match k:
        case 1:
            length = len(matrix_1)
            result_matrix = [[0 for i in range(length)] for i in range(length)]
            for i in range(length):
                for j in range(length):
                    result_matrix[i][j] = matrix_1[j][i]
        case 2:
            length = len(matrix_1)
            result_matrix = [[0 for i in range(length)] for i in range(length)]
            for i in range(length):
                for j in range(length):
                    result_matrix[i][j] = matrix_1[-j - 1][-i - 1]
        case 3:
            length = len(matrix_1)
            result_matrix = [[0 for i in range(length)] for i in range(length)]
            for i in range(length):
                for j in range(length):
                    result_matrix[i][j] = matrix_1[i][-j - 1]
        case 4:
            length = len(matrix_1)
            result_matrix = [[0 for i in range(length)] for i in range(length)]
            for i in range(length):
                for j in range(length):
                    result_matrix[i][j] = matrix_1[-i - 1][j]
    matrixprint(result_matrix)

def determinant(matrix):
    if len(matrix) != len(matrix[0]) or len(matrix) > 3:
        print("ERRor")
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if len(matrix) == 3:
        return matrix[0][0] * matrix[1][1] * matrix[2][2] + matrix[0][2] * matrix[1][0] * matrix[2][1] + matrix[0][1] * matrix[1][2] * matrix[2][0] - matrix[0][2] * matrix[1][1] * matrix[2][0] - matrix[0][0] * matrix[1][2] * matrix[2][1] - matrix[0][1] * matrix[1][0] * matrix[2][2]

mainmenu()
