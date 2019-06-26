#define a function diagonalReverse() that takes matrix and returns diagonal-reversed one:

a = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
b = [0,0,0],[0,0,0],[0,0,0]

def diagonalReverse(matrix):
    for i in range(len(a)):
        for j in range(len(a[0])):
            b[j][i] = a[i][j]
    for row in b:
        print(row)

diagonalReverse(a)
