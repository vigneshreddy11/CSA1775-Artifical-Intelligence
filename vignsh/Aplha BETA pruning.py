def alpha_beta(depth, node_index, is_max, values, alpha, beta, target_depth):
    """
    Alpha-Beta Pruning Algorithm.
    """
    if depth == target_depth:
        return values[node_index]

    if is_max:
        max_eval = float('-inf')
        for i in range(2):  # Binary tree, so two children
            eval = alpha_beta(depth + 1, node_index * 2 + i, False, values, alpha, beta, target_depth)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Prune
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(2):  # Binary tree, so two children
            eval = alpha_beta(depth + 1, node_index * 2 + i, True, values, alpha, beta, target_depth)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Prune
        return min_eval


def main():
    print("Alpha-Beta Pruning Example")
    num_leaf_nodes = int(input("Enter the number of leaf nodes (must be a power of 2): "))

    if (num_leaf_nodes & (num_leaf_nodes - 1)) != 0:
        print("Error: Number of leaf nodes must be a power of 2.")
        return

    print(f"Enter the {num_leaf_nodes} leaf node values:")
    values = [int(input(f"Value of leaf node {i+1}: ")) for i in range(num_leaf_nodes)]

    depth = len(bin(num_leaf_nodes)) - 3  # Compute depth based on leaf nodes
    optimal_value = alpha_beta(0, 0, True, values, float('-inf'), float('inf'), depth)

    print(f"The optimal value is: {optimal_value}")


if __name__ == "__main__":
    main()
