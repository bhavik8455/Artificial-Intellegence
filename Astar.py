import heapq
def display_board(board):
    for row in board:
        print(f"{' '.join(str(num) if num != 0 else '_'for num  in row)}")
    print()
def empty_tile(board):
    x,y = next((r,c) for r in range(3) for c in range(3) if board[r][c]==0)
    return x,y
def calculate_misplaced_tiles(initial_board,goal_board):
    return sum(initial_board[i][j] != goal_board[i][j] and initial_board[i][j] !=0 for i in range(3) for j in range(3))
def possible_moves(board):
    possible_move = []
    dictionary = {('UP',-1,0),('DOWN',1,0),('LEFT',0,-1),('RIGHT',0,1)}
    empty_x,empty_y = empty_tile(board)
    for move,x,y in dictionary:
        new_x,new_y = empty_x+x,empty_y+y
        if 0 <= new_x <3 and 0 <= new_y < 3:
            new_board = [row[:] for row in board]
            new_board[empty_x][empty_y],new_board[new_x][new_y] = new_board[new_x][new_y],0
            possible_move.append((new_board,move))
    return possible_move
def solve_puzzle(initial_board,goal_board):
    visited = set()
    initial_h_value = calculate_misplaced_tiles(initial_board,goal_board)
    queue = [(initial_h_value,0,initial_board,[],0,initial_h_value)]
    heapq.heapify(queue)
    move_counter = 0
    while queue:
        f_value,_,board,path_so_far,g_value,h_value = heapq.heappop(queue)
        board_tuple = tuple(tuple(row) for row in board)
        if board_tuple in visited:
            continue
        visited.add(board_tuple)
        if board == goal_board :
            return path_so_far,g_value,h_value,f_value
        for new_board,move_name in possible_moves(board):
            new_board_tuple = tuple(tuple(row) for row in new_board)
            if new_board_tuple in visited:
                continue
            new_g_value = g_value + 1
            new_h_value = calculate_misplaced_tiles(new_board,goal_board)
            new_f_value = new_g_value + new_h_value
            new_path = path_so_far + [(move_name,new_board,new_g_value,new_h_value)]
            move_counter +=1
            heapq.heappush(queue,(new_f_value,move_counter,new_board,new_path,new_g_value,new_h_value))  
    return None,0,0,0
def  display_function(path,initial_state,initial_g,initial_h,initial_f):
    print("The Iitial state is ")
    print(f"g(n): {initial_g} | h(n): {initial_h} | f(n): {initial_f}")
    display_board(initial_state)
    print("\nSolution Steps")
    for move,board,g,h in path:
         print(f"MOVE : {move}  | g(n): {g} | h(n): {h} | f(n): {g+h}")
         display_board(board)
    print("Goal Achived")       
print("Enter the Initial State : ")
initial_state = []
for i in range(3):
    initial_state.append(list(map(int,input(f"Enter the row {i+1} : ").strip().split())))
goal_state = []
print("Enter the Goal State : ")
for i in range(3):
    goal_state.append(list(map(int,input(f"Enter the row {i+1} : ").strip().split())))
path,initial_g,initial_h,initial_f = solve_puzzle(initial_state,goal_state)
if path is not None:
    display_function(path,initial_state,initial_g,initial_h,initial_f)
else: print("Solution not found")