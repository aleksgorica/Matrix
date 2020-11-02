from Matrix import Matrix
import random
n_rows = input("Enter number of rows ")
n_columns = input("Enter number of columns")

matrix = Matrix(n_columns, n_rows)
matrix.printMatrix()
#matrix.fillMatrix()
#matrix.transpose()
""" matrix.printMatrix()
matrix.switchRows(1,2)
matrix.printMatrix()
matrix.multiplyRow(2, 5)
matrix.printMatrix()
matrix.printMatrix() """
matrix.gauss_elimination()
matrix.printMatrix()
""" 
def printMatrix():
    print("-"*20)
    mat_str = ""
    for row in matrix:
        mat_str += "| "
        for element in row:
            mat_str += str(element)
            mat_str += " "
        mat_str += "|\n"
    mat_str += "-"*20
    print(mat_str)
 """
""" 
def generate
for i in range(n_rows):
    row = []
    for j in range(n_columns):
        row.append(input())
    matrix.append(row)
    printMatrix()

print(matrix)
 """