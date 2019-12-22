sudoku = [  [0,2,0,0,0,0,0,0,0],
            [0,0,0,6,0,0,0,0,3],
            [0,7,4,0,8,0,0,0,0],
            [0,0,0,0,0,3,0,0,2],
            [0,8,0,0,4,0,0,1,0],
            [6,0,0,5,0,0,0,0,0],
            [0,0,0,0,1,0,7,8,0],
            [5,0,0,0,0,9,0,0,0],
            [0,0,0,0,0,0,0,4,0]]

#Function to find an empty cell (0) within the puzzle.
#If there isn't any empty cell then the puzzle is solved
def find_empty():
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0:
                return (i, j)  # row, col

    return None

def solve(x, y):
    find = find_empty()
    if not find:
        return True
    else:
        row, col = find

    for num in range(1, 10):
        #lambda function to check if the number that we are trying to put into the empty cell is valid
        valid = lambda x, y, num: (not sameSquare(x, y, num) and not sameRow(x, y, num) and not sameCol(x, y, num))

        if valid(row, col, num):
            #place number into the cell
            sudoku[row][col] = num

            #move onto the next cell
            if solve(row, col): return True
            sudoku[row][col] = 0

    # enable backtracking
    return False

#Function to check if there is more than more of the same number within the same row
def sameRow(x, y, num):
    for i in range(0, 9):
        if(sudoku[x][i] == num): return True
    return False

#Function to check if there is more than more of the same number within the same column
def sameCol(x, y, num):
    for i in range(0, 9):
        if(sudoku[i][y] == num): return True
    return False

#Function to check if there is more than more of the same number within the same submatrix/square within the puzzle
def sameSquare(x, y, num):

    #find the starting location of the submatrix that we are checking for duplicates
    row_start = (x // 3) * 3
    col_start = (y // 3) * 3;

    for i in range(row_start, row_start+3):
        for j in range(col_start, col_start+3) :
            if(sudoku[i][j] == num): return True
    return False

#print out the sudoku puzzle
def printSudoku():
    for row in sudoku:
        print(row)

#driver function for the code
if __name__ == "__main__":
    printSudoku()
    solve(0,0)
    print("----------------------------")
    printSudoku()

