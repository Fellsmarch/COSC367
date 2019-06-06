def max_value(tree, alpha=float('-inf'), beta=float('inf')):
    """Finds the max utility from children nodes using alpha-beta-pruning"""
    max_utility = float("-inf")
    
    if (is_terminal(tree)):
        return tree
    else:
        for i, node in enumerate(tree):
            max_utility = max(max_utility, min_value(node, alpha, beta))
            
            if max_utility >= beta:
                if tree[i+1:]:
                    print("Pruning:", ", ".join(map(str, tree[i+1:])))                
                return max_utility
            
            alpha = max(alpha, max_utility)
        return max_utility    

def min_value(tree, alpha=float('-inf'), beta=float('inf')):
    """Finds the min utility from children nodes using alpha-beta-pruning"""
    min_utility = float("inf")
    
    if (is_terminal(tree)):
        return tree
    else:
        for i, node in enumerate(tree):
            min_utility = min(min_utility, max_value(node, alpha, beta))
            
            if min_utility <= alpha:
                if tree[i+1:]:
                    print("Pruning:", ", ".join(map(str, tree[i+1:])))   
                return min_utility
            
            beta = min(beta, min_utility)
        return min_utility    
    
def is_terminal(node):
    """Returns true if the node/state given is a terminal state (leaf node)
    and false if otherwise"""
    return isinstance(node, int)