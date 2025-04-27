import numpy as np
def bfs(matrix,start,nodes,labels,traversal = []):
    visited = [False] * nodes
    queue = [start]
    visited[start] = True
    while queue:
        node = queue.pop(0)
        traversal.append(labels[node])
        print(f"Visting the node {labels[node]} , QUEUE : {' '.join(labels[n] for n in queue)}")
        for neighbour in range(nodes):
            if matrix[node][neighbour] == 1 and  not visited[neighbour]:
                queue.append(neighbour)
                visited[neighbour] = True
                print(f"Adding the node {labels[neighbour]} in queue , QUEUE : {' '.join(labels[n] for n in queue)}")
    print(f"The Final BFS Traversal  is {'->'.join(traversal)}")
def dfs(matrix,start,nodes,labels,traversal = []):
    visited = [False]*nodes
    stack = [start]
    while stack:
        node = stack.pop()
        if not visited[node]:
            traversal.append(labels[node],)
            visited[node] = True
            print(f"Visiting the node {labels[node]} , STACK : {' '.join(labels[n] for n in stack)}")
            for neighbour in range(nodes-1,-1,-1):
                if matrix[node][neighbour] == 1 and not visited[neighbour] and neighbour not in stack:
                    stack.append(neighbour)
                    print(f"Adding the node {labels[neighbour]} in stack , STACK : {' '.join(labels[n] for n in stack)}")
    print(f"The Final DFS Traversal  is {' ->'.join(traversal)}")
nodes = int(input("Enter the no. of nodes : "))
matrix = np.zeros((nodes,nodes),dtype=int)
print("Enter the adjancy matrix")
for i in range(nodes):
    matrix[i] = list(map(int,input().split()))
start_node = input("Enter the starting node (A-G) : ")
start = ord(start_node) - ord('A')
labels = ['A','B','C','D','E','F','G']
print("The BFS is\n ",bfs(matrix,start,nodes,labels,traversal = []))
print("\n\nThe DFS is \n",dfs(matrix,start,nodes,labels,traversal = []))