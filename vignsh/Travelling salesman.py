

import sys
from itertools import permutations

def travelling_salesman(graph, start):
    nodes = [i for i in range(len(graph)) if i != start]

    min_cost = sys.maxsize
    best_path = []

    for perm in permutations(nodes):
        current_cost = 0
        k = start
        for j in perm:
            current_cost += graph[k][j]
            k = j
        current_cost += graph[k][start]

        if current_cost < min_cost:
            min_cost = current_cost
            best_path = [start] + list(perm) + [start]

    return best_path, min_cost

def main():
    # Input the number of nodes
    num_nodes = int(input("Enter the number of nodes: "))
    print("Enter the cost matrix row by row:")

    graph = []
    for _ in range(num_nodes):
        row = list(map(int, input().split()))
        graph.append(row)

    start_node = int(input("Enter the starting node (0-indexed): "))

    best_path, min_cost = travelling_salesman(graph, start_node)

    print("Optimal Path:", " -> ".join(map(str, best_path)))
    print("Minimum Cost:", min_cost)

if __name__ == "__main__":
    main()
import sys
from itertools import permutations

def travelling_salesman(graph, start):
    nodes = [i for i in range(len(graph)) if i != start]

    min_cost = sys.maxsize
    best_path = []

    for perm in permutations(nodes):
        current_cost = 0
        k = start
        for j in perm:
            current_cost += graph[k][j]
            k = j
        current_cost += graph[k][start]

        if current_cost < min_cost:
            min_cost = current_cost
            best_path = [start] + list(perm) + [start]

    return best_path, min_cost

def main():
    # Input the number of nodes
    num_nodes = int(input("Enter the number of nodes: "))
    print("Enter the cost matrix row by row:")

    graph = []
    for _ in range(num_nodes):
        row = list(map(int, input().split()))
        graph.append(row)

    start_node = int(input("Enter the starting node (0-indexed): "))

    best_path, min_cost = travelling_salesman(graph, start_node)

    print("Optimal Path:", " -> ".join(map(str, best_path)))
    print("Minimum Cost:", min_cost)

if __name__ == "__main__":
    main()
