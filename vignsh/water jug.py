from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque([(0, 0)])  # Start with both jugs empty
    steps = []

    while queue:
        jug1, jug2 = queue.popleft()

        # If we've already visited this state, skip it
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))
        steps.append((jug1, jug2))

        # Check if we've reached the target amount
        if jug1 == target or jug2 == target:
            for step in steps:
                print(step)
            return True

        # Generate all possible next states
        next_states = [
            (jug1_capacity, jug2),              # Fill jug1
            (jug1, jug2_capacity),              # Fill jug2
            (0, jug2),                          # Empty jug1
            (jug1, 0),                          # Empty jug2
            (min(jug1 + jug2, jug1_capacity),   # Pour jug2 into jug1
             max(0, jug2 - (jug1_capacity - jug1))),
            (max(0, jug1 - (jug2_capacity - jug2)),   # Pour jug1 into jug2
             min(jug1 + jug2, jug2_capacity))
        ]

        # Add valid next states to the queue
        for state in next_states:
            if state not in visited:
                queue.append(state)

    print("No solution.")
    return False

# Input
jug1_capacity = int(input("Enter capacity of jug1: "))
jug2_capacity = int(input("Enter capacity of jug2: "))
target = int(input("Enter the target amount: "))

# Solve
print("\nSteps to solve the water jug problem:")
water_jug_problem(jug1_capacity, jug2_capacity, target)
