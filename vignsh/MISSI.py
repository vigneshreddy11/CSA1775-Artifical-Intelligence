def is_valid(state):
    """Check if the given state is valid."""
    m_left, c_left, m_right, c_right, _ = state  # Ignore the boat position
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if (m_left > 0 and m_left < c_left) or (m_right > 0 and m_right < c_right):
        return False
    return True


def solve_missionaries_cannibals(m, c, boat_capacity):
    """Solve the Missionaries and Cannibals problem."""
    start = (m, c, 0, 0, 'left')
    goal = (0, 0, m, c, 'right')
    queue = [(start, [])]
    visited = set()

    while queue:
        (state, path) = queue.pop(0)
        if state == goal:
            return path + [state]

        if state in visited:
            continue
        visited.add(state)

        m_left, c_left, m_right, c_right, boat = state

        # Generate possible moves
        moves = [
            (m, c)
            for m in range(boat_capacity + 1)
            for c in range(boat_capacity + 1)
            if 1 <= m + c <= boat_capacity
        ]

        for m, c in moves:
            if boat == 'left':  # Move from left to right
                new_state = (m_left - m, c_left - c, m_right + m, c_right + c, 'right')
            else:  # Move from right to left
                new_state = (m_left + m, c_left + c, m_right - m, c_right - c, 'left')

            if is_valid(new_state):
                queue.append((new_state, path + [state]))
    return None


# Input
m = int(input("Enter the number of missionaries: "))
c = int(input("Enter the number of cannibals: "))
boat_capacity = int(input("Enter the boat capacity: "))

# Solve
solution = solve_missionaries_cannibals(m, c, boat_capacity)

# Output
if solution:
    print("\nSolution steps:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
