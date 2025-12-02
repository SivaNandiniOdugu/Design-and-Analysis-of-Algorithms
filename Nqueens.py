'''def print_board(B):
    for row in B:
        print(" ".join("Q" if col else "." for col in row))
    print()'''
def print_board(B):
    for i in range(len(B)):
        for j in range(len(B)):
            if B[i][j]==1:
                print('Q',end=" ")
            else:
                print('.',end=" ")
        print()   
    print()

def feasible(B, r, c,n):
    for i in range(r-1,-1,-1):
        j = r-i
        if (B[i][c]) or ((c-j>=0) and B[i][c-j]) or ((c+j<n) and B[i][c+j]):
            return False
    return True

def solve_n_queens(board, row, n):
    if row == n:
        print_board(board)
        #return False #false means Continue
    for col in range(n):
        if feasible(board, row, col,n):
            board[row][col] = 1
            ok = solve_n_queens(board, row + 1, n)
            board[row][col] = 0  # backtrack
    #return False

def n_queens(n):
    board = [[0]*n for _ in range(n)]
    solve_n_queens(board, 0, n)

# Example usage
n_queens(4)