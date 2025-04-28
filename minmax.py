import math
PLAYER,OPPONENT,EMPTY = 'X','O','_'
board = [[EMPTY for _ in range(3)] for _ in range(3)]
print('\n'.join(' '.join(row)for row in board),'\n')
while any(EMPTY in row  for row in board):
    def check_winner():
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != EMPTY:
                return 1 if board[i][0]== PLAYER else -1
            if board[0][i] == board[1][i] == board[2][i] != EMPTY:
                return 1 if board[0][i]== PLAYER else -1
        if board[0][0] == board[1][1] == board[2][2] != EMPTY or board[0][2] == board[1][1] == board[2][0] != EMPTY:
            return 1 if board[1][1] == PLAYER else -1
        return 0
    def minmax(board,is_max):
        score = check_winner()
        if score != 0 or not any(EMPTY in row for row in board):
            return score
        best = -math.inf if is_max else math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER if is_max else OPPONENT
                    val = minmax(board,not is_max)
                    board[i][j] = EMPTY
                    best = max(best,val) if is_max else min (best,val)
        return best
    best_move,best_val =(-1,-1), -math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER 
                move_Val = minmax(board,False)
                board[i][j] = EMPTY
                print(f"The position {i},{j} has utility value {move_Val}")
                if move_Val > best_val:
                    best_move,best_val =(i,j), move_Val
    x,y = best_move
    board[x][y] = PLAYER
    print("AI Turns")
    print('\n'.join(' '.join(row)for row in board),'\n')
    result = check_winner()
    if result != 0 or not any(EMPTY in row for row in board):
        break
    while True:
        row,col = map(int,input("Enter the position i.e(row col): ").split())
        if 0 <= row < 3 and 0<= col <3 and board[row][col] ==EMPTY:
            board[row][col] = OPPONENT
            break
    print("\nAfter you move\n")
    print('\n'.join(' '.join(row)for row in board),'\n')
    if check_winner() != 0:
        break
result = check_winner()
print("AI WINS"if result == 1 else "YOU WINS" if result == -1 else "GAME DRAW" )          