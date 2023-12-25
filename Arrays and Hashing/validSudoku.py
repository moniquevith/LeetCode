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
    box_digits = {}
    for row in range(9):
        for col in range(9):
            return

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

isValidSudoku(board)