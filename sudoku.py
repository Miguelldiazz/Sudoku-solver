import random
import math


class Sudoku():

    def __init__(self, rows, cols, missing):
        self.rows = rows
        self.cols = cols
        self.missing = missing
        self.board = [[0 for x in range(cols)] for y in range(rows)]
        
        self.submatrices = int(math.sqrt(cols))

        #fill the diagonal 3x3 matrices
        for i in range(0, self.cols, self.submatrices):
            self.fill_box(i, i)

        self.fill_remaining(self.submatrices, 0)
        self.remove_digits()


    
    def __str__(self):
        ret = ''
        for x in self.board:
            for y in x:
                ret += str(y) + ' '
            ret += '\n'
        
        return ret
    
    #fills randomly a 3x3 submatrix with numbers from 1 to 9
    def fill_box(self, col, row):
        used = []
        for i in range(3):
            for j in range(3):
                n = random.randint(1, 9)
                while n in used:
                    n = random.randint(1, 9)
                used.append(n)
                self.board[i + col][j + row] = n

    #fills the remaining cells with valid numbers
    def fill_remaining(self, col, row):
        if col >= self.cols and row < self.cols - 1:
            row += 1
            col = 0
        
        if row >= self.cols and col >= self.cols:
            return True

        if row < self.submatrices:
            if col < self.submatrices:
                col = self.submatrices
        elif row < self.cols - self.submatrices:
            if col == self.submatrices:
                col = col + self.submatrices
        else:
            if col == self.cols - self.submatrices:
                row += 1
                col = 0
                if row >= self.cols:
                    return True

        for i in range(1, 10):
            if self.safe(col, row, i):
                self.board[row][col] = i
                if self.fill_remaining(col + 1, row):
                    return True
                self.board[row][col] = 0

        return False

    def safe(self, col, row, num):
        return self.not_in_col(col, num) and self.not_in_row(row, num) and self.not_in_box(col - col % self.submatrices, row - row % self.submatrices, num)


    def not_in_col(self, col, num):
        for i in range(self.cols):
            if self.board[i][col] == num:
                return False
        return True

    def not_in_row(self, row, num):
        return num not in self.board[row]

    def not_in_box(self, col, row, num):
        for i in range(self.submatrices):
            for j in range(self.submatrices):
                if self.board[row + i][col + j] == num:
                    return False
        return True

    def remove_digits(self):
        count = self.missing
        while count != 0:
            row = random.randint(0, self.cols - 1)
            col = random.randint(0, self.cols - 1)

            if self.board[row][col] != 0:
                count -= 1
                self.board[row][col] = 0


    #solves the sudoku using backtracking
    def solve(self):
        coordenates = [0, 0]
        if not self.unsolved(coordenates):
            return True

        
        row = coordenates[0]
        col = coordenates[1]

        for i in range(1, 10):
            if self.safe(col, row, i):
                self.board[row][col] = i

                if self.solve():
                    return True

                self.board[row][col] = 0
        return False

    
    def unsolved(self, coordenates):
        for i in range(self.cols):
            for j in range(self.rows):
                if self.board[i][j] == 0:
                    coordenates[0] = i
                    coordenates[1] = j
                    return True
        return False



