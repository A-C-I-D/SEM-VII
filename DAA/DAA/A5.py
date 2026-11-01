def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()


def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueen(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve_nqueen(board, row + 1, n):
                return True

            board[row][col] = 0  # Backtracking

    return False


n = int(input("Enter the value of N: "))

board = [[0 for j in range(n)] for i in range(n)]

# Place first queen
board[0][0] = 1

if solve_nqueen(board, 1, n):
    print("\nN-Queens Solution:")
    print_board(board, n)
else:
    print("Solution does not exist")