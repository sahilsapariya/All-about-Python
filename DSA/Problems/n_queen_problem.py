"""
    What is the N-Queens problem?
    Ans. we try to place N chess queens on an NxN chessboard such that
         no two queens attack each other. 
         Queens can attack each other 
         if they share the same row, column, or diagonal on the board.
"""

class Nqueens:

    def __init__(self, n) -> None:
        self.n = n
        self.columns = [None] * n
        self.count = 0

    def place_queen(self, row, column):
        self.columns[row] = column

    def remove_queen(self, row):
        self.columns[row] = None

    def is_safe(self, row, column):
        for i in range(row):
            if (
                self.columns[i] == column or
                self.columns[i] - i == column - row or
                self.columns[i] + i == column + row
            ):
                return False
        return True
    
    def solve(self, row=0):
        if row == self.n:
            self.count += 1
            return
        for col in range(self.n):
            if self.is_safe(row, col):
                self.place_queen(row, col)
                self.solve(row + 1)
                self.remove_queen(row)
    
    def get_count(self):
        self.solve()
        return self.count
    
if __name__ == "__main__":
    n_queens = Nqueens(8)
    print(n_queens.get_count())

# output:
# 92