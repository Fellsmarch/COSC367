
def max_value(tree):
    """Finds the max utility from children nodes"""
    max_utility = float("-inf")
    
    if (is_terminal(tree)):
        return tree
    else:
        #options = []
        for node in tree:
            #options.append(max_value(node))
            max_utility = max(max_utility, min_value(node))
        return max_utility
    
    
def min_value(tree):
    """Find the min utility from children nodes"""
    min_utility = float("inf")
    
    if (is_terminal(tree)):
        return tree
    else:
        #options = []
        for node in tree:
            #options.append(max_value(node))
            min_utility = min(min_utility, max_value(node))
        return min_utility
        
def is_terminal(node):
    """Returns true if the node/state given is a terminal state (leaf node)
    and false if otherwise"""
    return isinstance(node, int)


if __name__ == "__main__":
    
    print("Test case 1:")
    tree = 3
    print("Game tree:", tree)
    print("Root utility for maximiser:", max_value(tree))
    print("Root utility for minimiser:", min_value(tree))
    print()
    
    print("Test case 2:")
    tree = [1, 2, 3]
    print("Game tree:", tree)
    print("Root utility for maximiser:", max_value(tree))
    print("Root utility for minimiser:", min_value(tree))
    print()
    
    print("Test case 3:")
    tree = [1, 2, [3]]
    print("Game tree:", tree)
    print("Root utility for maximiser:", max_value(tree))
    print("Root utility for minimiser:", min_value(tree))
    print()
    
    print("Test case 4:")
    tree = [[1, 2], [3]]
    print("Game tree:", tree)
    print("Root utility for maximiser:", max_value(tree))
    print("Root utility for minimiser:", min_value(tree))
    print()
    
    print("Test case 5:")
    tree = [[1, 2], [3, 4]]
    print("Game tree:", tree)
    print("Root utility for maximiser:", max_value(tree))
    print("Root utility for minimiser:", min_value(tree))
    print()
    
    print("Test case 6:")
    tree = [[2, 3, 4], [1, 100, -100]]
    print("Game tree:", tree)
    print("Root utility for maximiser:", max_value(tree))
    print("Root utility for minimiser:", min_value(tree))
    print()
    
    print("Test case 7:")
    # From the lecture notes
    tree = [[3, 12, 8], [2, 4, 6], [14, 5, 2]]
    print("Game tree:", tree)
    print("Root utility for maximiser:", max_value(tree))
    print("Root utility for minimiser:", min_value(tree))
    print()
    
    print("Test case 8:")
    tree = [[[3, 12], 8], [2, [4, 6]], [14, 5, 2]]
    print("Game tree:", tree)
    print("Root utility for maximiser:", max_value(tree))
    print("Root utility for minimiser:", min_value(tree))
    print()
    
    print("Test case 9:")
    tree = [[1, 4], [3, 5], [2]]
    print("Game tree:", tree)
    print("Root utility for maximiser:", max_value(tree))
    print("Root utility for minimiser:", min_value(tree))
    print()
    
     
    
    