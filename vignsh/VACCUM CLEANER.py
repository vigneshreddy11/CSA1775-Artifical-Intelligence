from collections import deque

# Vacuum Cleaner Function
def vacuum_cleaner(grid):
    """Simulates a vacuum cleaner cleaning a grid."""
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    if rows == 0 or cols == 0:
        print("Grid is empty.")
        return

    # Simulate cleaning
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Clean the tile if dirty
                print(f"Cleaning tile at ({i}, {j}).")
                grid[i][j] = 0  # Clean the dirt
            else:
                print(f"Tile at ({i}, {j}) is already clean.")

    print("\nAll tiles are clean. Final grid:")
    for row in grid:
        print(row)


# Input the grid
print("Enter the grid dimensions (rows and columns):")
rows = int(input("Rows: "))
cols = int(input("Columns: "))

print("Enter the grid (0 for clean, 1 for dirty):")
grid = []
for _ in range(rows):
    row = list(map(int, input().split()))
    if len(row) != cols:
        print("Invalid input: Each row must have exactly", cols, "columns.")
        exit()
    grid.append(row)

# Call the vacuum cleaner function
vacuum_cleaner(grid)


# BFS Function
def bfs(graph, start):
    visited = set()  # To keep track of visited nodes
    queue = deque([start])  # Initialize the queue with the start node
    traversal = []  # List to store the BFS traversal order

    while queue:
        node = queue.popleft()  # Remove the first node from the queue
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            traversal.append(node)  # Add the node to the traversal list
            queue.extend([n for n in graph[node] if n not in visited])  # Add unvisited neighbors to the queue

    return traversal


# Input: Graph and starting node
graph = {}
num_nodes = int(input("\nEnter the number of nodes in the graph: "))

print("Enter the neighbors for each node (comma-separated):")
for _ in range(num_nodes):
    node = input("Node: ").strip()
    neighbors = input(f"Neighbors of {node} (comma-separated): ").strip().split(",")
    graph[node] = [neighbor.strip() for neighbor in neighbors if neighbor.strip()]

start_node = input("Enter the starting node for BFS: ").strip()

# Perform BFS
if start_node not in graph:
    print("Starting node not in graph!")
else:
    result = bfs(graph, start_node)
    print("BFS Traversal:", result)
