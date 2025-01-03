import math

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    # Base case: if the current depth is the target depth, return the score at this node
    if curDepth == targetDepth:
        return scores[nodeIndex]

    # If it's the maximizing player's turn
    if maxTurn:
        return max(minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth))
    # If it's the minimizing player's turn
    else:
        return min(minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth))

def main():
    # Get number of leaf nodes from the user
    num_leaf_nodes = int(input("Enter the number of leaf nodes (must be a power of 2): "))
    
    # Check if the number of leaf nodes is a power of 2
    if (num_leaf_nodes & (num_leaf_nodes - 1)) != 0 or num_leaf_nodes <= 0:
        print("Invalid number of leaf nodes! It should be a positive power of 2.")
        return

    # Get the leaf node scores from the user
    scores = []
    print(f"Enter the scores for the {num_leaf_nodes} leaf nodes:")
    for i in range(num_leaf_nodes):
        score = int(input(f"Score for leaf node {i+1}: "))
        scores.append(score)
    
    # Calculate the depth of the game tree
    treeDepth = int(math.log(num_leaf_nodes, 2))

    # Start the minimax algorithm from depth 0 and index 0 with maximizing player's turn
    optimal_value = minimax(0, 0, True, scores, treeDepth)

    # Print the result
    print("The optimal value is:", optimal_value)

if __name__ == "__main__":
    main()
