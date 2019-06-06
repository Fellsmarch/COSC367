import itertools

def neighbours(assignment):
    """Takes an assignment of the n-queens problem and yields a neighbour of
       that assignment (a neighbour having only two numbers swapped)"""    
    for index_1, index_2 in itertools.combinations(range(len(assignment)), 2):
        new_assign = list(assignment)
        new_assign[index_1], new_assign[index_2] = new_assign[index_2], new_assign[index_1]
        yield tuple(new_assign)
        
"""Write a function neighbours that takes a total assignment for an n-queen problem and returns a sequence (list or iterator) of total assignments that are the neighbours of the current assignment. A neighbour is obtained by swapping the position of two numbers in the given permutation.

Like before, the assignment will be given in the form of a sequence (tuple more specifically). The assignment is a permutation of numbers from 1 to n. The value of n must be inferred from the given assignment.

Because of the choice of representation (the permutation of numbers from 1 to n) the concept of neighbourhood in this question is different from that in the example given in the lecture notes. The representation we use does not allow to have repeated numbers in a sequence, therefore we define a neighbouring assignment to be one that can be obtained by swapping the position of two numbers in the current assignment."""