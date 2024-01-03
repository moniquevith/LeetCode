def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    # check if rows have no reps 
    row_digits = {}
    for row in range(9):
        for col in range(9):
            if board[row][col] == ".":
                continue
            else: 
                if board[row][col] in row_digits:
                    print("not valid row")
                else: 
                    row_digits[board[row][col]] = 1
        row_digits = {}

    # check if cols have no reps 
    column_digits = {}
    for col in range(9):
        for row in range(9):
            if board[row][col] == ".":
                continue
            else: 
                if board[row][col] in column_digits:
                    print("not valid col")
                else: 
                    column_digits[board[row][col]] = 1
        column_digits = {}

    # check if 3x3 boxes have reps 
    box_digits = {} # {(0,0): [1,..,9], (0,1): [1,..,9] }
    for row in range(9):
        for col in range(9):
            if board[row][col] == ".":
                continue
            else:
                if (row // 3, col // 3) in box_digits and board[row][col] in box_digits[(row // 3, col // 3)]: # check if the key pair value exists and if the current value is in the list
                    print("not valid square")
                else: # if current value not already in list, add it
                    new_list = box_digits.get((row // 3, col // 3), []) + [board[row][col]] # add the current value to the list of that square, if that key doesnt exist make it equal to []
                    box_digits[(row // 3, col // 3)] = new_list # change that key pair value to the new list 

    return True

board = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]

isValidSudoku(board)