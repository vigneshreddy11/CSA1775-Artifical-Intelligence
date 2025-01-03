from heapq import heappush, heappop
from copy import deepcopy

n = 3  # size of the puzzle
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # directions to move the empty tile

class Node:
    def __init__(self, parent, mat, empty_pos, level, cost):
        self.parent = parent
        self.mat = mat
        self.empty_pos = empty_pos
        self.level = level
        self.cost = cost  # cost is the heuristic cost (misplaced tiles)
        
    def __lt__(self, other):
        return (self.level + self.cost) < (other.level + other.cost)  # A* cost = level + heuristic cost

def calculate_cost(mat, final):
    """Calculate the heuristic cost (number of misplaced tiles)."""
    return sum(
        mat[i][j] != final[i][j] and mat[i][j] != 0 for i in range(n) for j in range(n)
    )

def generate_node(mat, empty_pos, new_pos, level, parent, final):
    """Generate a new node by moving the empty tile."""
    new_mat = deepcopy(mat)
    x1, y1 = empty_pos
    x2, y2 = new_pos
    new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]
    cost = calculate_cost(new_mat, final)
    return Node(parent, new_mat, new_pos, level + 1, cost)

def is_safe(x, y):
    """Check if the position is within the grid."""
    return 0 <= x < n and 0 <= y < n

def print_path(node):
    """Print the path from the root to the solution."""
    if node is None:
        return
    print_path(node.parent)
    for row in node.mat:
        print(*row)
    print()

def solve(initial, empty_pos, final):
    """Solve the puzzle using the A* algorithm."""
    pq = []  # priority queue
    visited = set()  # set to track visited states
    root = Node(None, initial, empty_pos, 0, calculate_cost(initial, final))
    heappush(pq, root)

    while pq:
        curr = heappop(pq)

        # If the current state is the solution, print the path and exit
        if curr.cost == 0:
            print("Solution:")
            print_path(curr)
            return

        visited.add(tuple(tuple(row) for row in curr.mat))  # add state to visited set

        x, y = curr.empty_pos
        for dx, dy in directions:
            new_pos = (x + dx, y + dy)
            if is_safe(*new_pos):
                child = generate_node(curr.mat, curr.empty_pos, new_pos, curr.level, curr, final)
                if tuple(tuple(row) for row in child.mat) not in visited:
                    heappush(pq, child)

    print("No solution exists.")

# User input
print("Enter the initial 3x3 puzzle configuration (use 0 for the empty tile):")
initial = [list(map(int, input().split())) for _ in range(n)]

print("Enter the final 3x3 puzzle configuration:")
final = [list(map(int, input().split())) for _ in range(n)]

empty_pos = next((i, j) for i in range(n) for j in range(n) if initial[i][j] == 0)

solve(initial, empty_pos, final)
