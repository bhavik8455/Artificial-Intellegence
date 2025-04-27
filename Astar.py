import heapq

def misplaced_tiles(state, goal):
    return sum(state[i][j] != goal[i][j] and state[i][j] != 0 for i in range(3) for j in range(3))
def get_neighbors(state):
    neighbors = []
    x, y = next((r, c) for r in range(3) for c in range(3) if state[r][c] == 0)
    for move, (dx, dy) in {'Up': (-1, 0), 'Down': (1, 0), 'Left': (0, -1), 'Right': (0, 1)}.items():
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append((new_state, move))
    return neighbors
def a_star_search(initial, goal):
    open_list = []
    closed_set = set()
    counter = 0
    node = (misplaced_tiles(initial, goal), 0, misplaced_tiles(initial, goal), initial, None, "")
    nodes = [node] 
    heapq.heappush(open_list, (node[0], counter, 0))
    while open_list:
        _, _, node_idx = heapq.heappop(open_list)
        f_cost, depth, heuristic, state, parent_idx, move = nodes[node_idx]
        if state == goal:
            path = []
            current_idx = node_idx
            while nodes[current_idx][4] is not None: 
                curr_node = nodes[current_idx]
                path.append((curr_node[5], curr_node[3], curr_node[1], curr_node[2]))
                current_idx = curr_node[4]
            return path[::-1], 0, nodes[0][2], nodes[0][0]
        closed_set.add(tuple(map(tuple, state)))
        for new_state, move in get_neighbors(state):
            if tuple(map(tuple, new_state)) not in closed_set:
                counter += 1
                new_depth = depth + 1
                new_h = misplaced_tiles(new_state, goal)
                new_f = new_depth + new_h
                new_node = (new_f, new_depth, new_h, new_state, node_idx, move)
                nodes.append(new_node)
                heapq.heappush(open_list, (new_f, counter, len(nodes) - 1))
    
    return None, 0, 0, 0

def print_solution(path, initial, g, h, f):
    format_row = lambda row: " ".join(str(num) if num != 0 else " " for num in row)
    print("Initial State:")
    print(f"g(n): {g} | h(n): {h} | f(n): {f}")
    for row in initial:
        print(format_row(row))
    print("\nSolution Steps:")
    for move, state, g, h in path:
        print(f"\nMove: {move} | g(n): {g} | h(n): {h} | f(n): {g + h}")
        for row in state:
            print(format_row(row))
    print("\nGoal Reached!")
def read_state(prompt):
    print(prompt)
    return [list(map(int, input(f"Enter row {i+1} : ").strip().split())) for i in range(3)]

initial_state = read_state("Enter the Initial State :")
goal_state = read_state("\nEnter the Goal State :")
    
result = a_star_search(initial_state, goal_state)
if result[0] is not None:
    solution_path, initial_g, initial_h, initial_f = result
    print_solution(solution_path, initial_state, initial_g, initial_h, initial_f)
else:
    print("No solution found.")