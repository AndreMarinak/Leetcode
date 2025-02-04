def is_valid_sudoku(board):
    # Check rows
    for row in range(len(board)):  
        seen = set()
        for col in range(len(board[row])):  
            if board[row][col] == ".":
                continue
            if board[row][col] in seen:
                return False  # Duplicate found in the row
            seen.add(board[row][col])

    # Check columns
    for col in range(len(board)):  
        seen = set()
        for row in range(len(board)):  
            if board[row][col] == ".":
                continue
            if board[row][col] in seen:
                return False  # Duplicate found in the column
            seen.add(board[row][col])

    # Check 3x3 sub-boxes
    for square in range(9):
        seen = set()
        for i in range(3):
            for j in range(3):
                row = (square // 3) * 3 + i
                col = (square % 3) * 3 + j
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False  # Duplicate found in the 3x3 box
                seen.add(board[row][col])

    return True  # If no duplicates found, the board is valid

# Test Cases
board1 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(is_valid_sudoku(board1))  # Expected Output: True

board2 = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],  # Duplicate "8" in column
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(is_valid_sudoku(board2))  # Expected Output: False
