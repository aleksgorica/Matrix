import random
import sys 
class Matrix:
    def __init__(self, cols, rows):
        self.cols = int(cols)
        self.rows = int(rows)
        self.elements = self.blankMatrix(self.rows, self.cols, rand=True)


    def printMatrix(self, matrix=None):
        if matrix == None:
            matrix = self.elements
        print("-"*20)
        mat_str = ""
        for row in matrix:
            mat_str += "| "
            for element in row:
                mat_str += "{:12}".format(str(element))
                mat_str += " "
            mat_str += "|\n"
        mat_str += "-"*20
        print(mat_str)

    def blankMatrix(self, rows, cols, rand=False, val=0):
        value = val
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                if random:
                    value = random.randint(1, 10)
                row.append(value)
            matrix.append(row)
        return matrix
    
    def fillMatrix(self):
        print(len(self.elements))
        for i in range(len(self.elements)):
            for j in range(len(self.elements[i])):
                while True:

                    inp = input(f"Pos {i} {j}: ")
                    try:
                        inp = int(inp)
                        break
                    except ValueError:
                        try:
                            inp = float(inp)
                            break
                        except ValueError:
                            print("You have to enter a number")

                
                self.elements[i][j] = float(inp)
                self.printMatrix()

    def fillSelected(self, value, row, col):
        self.elements[row][col] = value

    def transpose(self):
        new_cols = self.rows
        new_rows = self.cols
        new_elements = self.blankMatrix(new_rows, new_cols)

        for i in range(self.rows):
            for j in range(self.cols):
                new_elements[j][i] = self.elements[i][j]
        self.cols = new_cols
        self.rows = new_rows
        self.elements = new_elements


    def switchRows(self, first, second):
        if first == second:
            return
        first_row = self.elements.pop(first)
        second_row = self.elements.pop(second-1)

        self.elements.insert(first, second_row)
        self.elements.insert(second, first_row)

    def multiplyRow(self, row, factor):
        for index in range(len(self.elements[row])):
            self.elements[row][index] = round(self.elements[row][index] * factor, 8)

    def addFacotredRowToRow(self, first, second, factor=1):
        print(self.elements, self.cols, self.rows, first, second)
        for index in range(self.cols):
            self.elements[second][index] += self.elements[first][index] * factor

    def gauss_elimination(self):
        for n in range(self.cols):
            row = -1
            for m in range(n, self.rows):
                if self.elements[m][n] != 0:
                    row = m
                    break
            if row == -1:
                continue
            print(f"multiply row {row}")
            self.multiplyRow(row, 1/ float(self.elements[row][n]))
            self.printMatrix()

            print(f"switch row {row} with {n}")
         
            self.switchRows(n, row)
            self.printMatrix()
            
            for m in range(n + 1, self.rows): 
                value = self.elements[m][n]
                if value != 0:
                    print(f"add factored row: {n} to {m} value {value}")
                    self.addFacotredRowToRow(n, m, -1 * value)
                    self.printMatrix()


       """  for n in range(self.cols - 1, 0 , -1):
                row = -1
                for m in range(self.rows, n, -1):
                    if self.elements[m][n] != 0:
                        row = m
                        break
                if row == -1:
                    continue
                print(f"multiply row {row}")
                self.multiplyRow(row, 1/ float(self.elements[row][n]))
                self.printMatrix()

                print(f"switch row {row} with {n}")
            
                self.switchRows(n, row)
                self.printMatrix()
                
                for m in range(n + 1, self.rows): 
                    value = self.elements[m][n]
                    if value != 0:
                        print(f"add factored row: {n} to {m} value {value}")
                        self.addFacotredRowToRow(n, m, -1 * value)
                        self.printMatrix()
             """

