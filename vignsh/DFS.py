from collections import defaultdict

def dfs(graph, start, visited):
    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def main():
    graph = defaultdict(list)

    # Input the number of edges
    num_edges = int(input("Enter the number of edges: "))

    # Input the edges of the graph
    for _ in range(num_edges):
        while True:
            edge = input("Enter an edge (format: u v): ").strip()
            if len(edge.split()) == 2:
                u, v = edge.split()
                graph[u].append(v)
                graph[v].append(u)  # Uncomment this line if the graph is undirected
                break
            else:
                print("Invalid input! Please enter exactly two values separated by a space.")

    # Input the starting node for DFS
    start_node = input("Enter the starting node for DFS: ").strip()

    visited = set()
    print("DFS Traversal:")
    dfs(graph, start_node, visited)

if __name__ == "__main__":
    main()
