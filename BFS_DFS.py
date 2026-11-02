
# Graph Traversal using BFS and DFS

vertices = ['A', 'B', 'C', 'D', 'E', 'F']
n = len(vertices)

# Adjacency Matrix for DFS
matrix = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0]
]

# Adjacency List for BFS
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'E'],
    'E': ['B', 'D'],
    'F': ['C']
}

# DFS using Adjacency Matrix
def dfs(start):
    visited = set()

    def traverse(node):
        index = vertices.index(node)
        visited.add(node)
        print(node, end=" ")

        for i in range(n):
            if matrix[index][i] == 1:
                next_node = vertices[i]
                if next_node not in visited:
                    traverse(next_node)

    traverse(start)

# BFS using Adjacency List
def bfs(start):
    visited = set([start])
    queue = [start]

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# Main Program
print("DFS Traversal:")
dfs('A')

print("\nBFS Traversal:")
bfs('A')
