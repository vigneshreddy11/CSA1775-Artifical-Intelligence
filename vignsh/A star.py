

import heapq

class Node:
    def __init__(self, position, g_cost=0, h_cost=0, parent=None):
        self.position = position
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost
        self.parent = parent

    def __lt__(self, other):
        return self.f_cost < other.f_cost

def a_star(start, goal, grid):
    open_list = []
    closed_list = set()
    start_node = Node(start, g_cost=0, h_cost=abs(start[0]-goal[0]) + abs(start[1]-goal[1]))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        closed_list.add(current_node.position)

        for neighbor in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = current_node.position[0] + neighbor[0], current_node.position[1] + neighbor[1]

            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != 1 and (nx, ny) not in closed_list:
                g_cost = current_node.g_cost + 1
                h_cost = abs(nx - goal[0]) + abs(ny - goal[1])
                neighbor_node = Node((nx, ny), g_cost=g_cost, h_cost=h_cost, parent=current_node)
                heapq.heappush(open_list, neighbor_node)

    return None

# Get input from user
def get_input():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    grid = []

    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1} (0 for free, 1 for blocked): ").split()))
        grid.append(row)

    start = tuple(map(int, input("Enter start position (x y): ").split()))
    goal = tuple(map(int, input("Enter goal position (x y): ").split()))

    return start, goal, grid

start, goal, grid = get_input()
path = a_star(start, goal, grid)

if path:
    print("Path found:", path)
else:
    print("No path found.")
