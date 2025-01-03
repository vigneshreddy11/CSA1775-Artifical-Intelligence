from constraint import Problem

def get_list_from_user(prompt, item_name):
    while True:
        try:
            items = input(prompt).split(",")
            items = [item.strip() for item in items if item.strip()]
            if items:
                return items
            else:
                print(f"Please enter at least one {item_name}.")
        except Exception as e:
            print(f"Error: {e}. Please try again.")

def get_adjacent_regions():
    adjacent_regions = []
    print("Enter adjacent regions as pairs (e.g., A-B). Type 'done' when finished:")
    while True:
        pair = input("Enter adjacency pair: ")
        if pair.lower() == "done":
            break
        try:
            region1, region2 = pair.split("-")
            region1, region2 = region1.strip(), region2.strip()
            if region1 in regions and region2 in regions:
                adjacent_regions.append((region1, region2))
            else:
                print(f"Error: One or both regions in the pair '{region1}-{region2}' are not in the defined regions list.")
        except ValueError:
            print("Invalid input. Enter pairs in the format A-B.")
    return adjacent_regions

# Initialize the problem
problem = Problem()

# Get user input for regions
regions = get_list_from_user("Enter the regions (comma-separated): ", "region")
colors = get_list_from_user("Enter the colors (comma-separated): ", "color")

# Add variables (regions) with possible colors
for region in regions:
    problem.addVariable(region, colors)

# Get adjacency pairs and add constraints
adjacent_regions = get_adjacent_regions()
for region1, region2 in adjacent_regions:
    problem.addConstraint(lambda r1, r2: r1 != r2, (region1, region2))

# Solve the problem
solutions = problem.getSolutions()

# Display solutions
if solutions:
    print("\nPossible solutions:")
    for i, solution in enumerate(solutions, 1):
        print(f"Solution {i}: {solution}")
else:
    print("No solution found.")
