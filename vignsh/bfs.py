from collections import deque

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
num_nodes = int(input("Enter the number of nodes in the graph: "))

print("Enter the neighbors for each node (comma-separated):")
for _ in range(num_nodes):
    node = input("Node: ").strip()
    # Split the neighbors by comma and remove leading/trailing spaces
    neighbors_input = input(f"Neighbors of {node} (comma-separated): ").strip()
    neighbors = [neighbor.strip() for neighbor in neighbors_input.split(",") if neighbor.strip()]
    graph[node] = neighbors

start_node = input("Enter the starting node for BFS: ").strip()

# Perform BFS
if start_node not in graph:
    print("Starting node not in graph!")
else:
    result = bfs(graph, start_node)
    print("BFS Traversal:", result)
