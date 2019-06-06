import itertools

def neighbours(assignment):
    """Takes an assignment of the n-queens problem and yields a neighbour of
       that assignment (a neighbour having only two numbers swapped)"""
    for index_1, index_2 in itertools.combinations(range(len(assignment)), 2):
        new_assign = list(assignment)
        new_assign[index_1], new_assign[index_2] = new_assign[index_2], new_assign[index_1]
        yield tuple(new_assign)

def conflict_count(assignment):
    """Takes an assignment of the n-queens problems and returns the number of
       conflicts in the assignment"""
    conflicts = 0
    for row_1, col_1 in enumerate(assignment):
        for row_2, col_2 in enumerate(assignment[row_1 + 1:]):
            #This block is required since splicing effectively creates a new list starting at index 0
            if row_1 == 0: 
                row_2 += 1 
            else: 
                row_2 += row_1 + 1
                
            dx, dy = abs(row_2 - row_1), abs(col_2 - col_1) #Find the differences
            
            if dx != 0 and dy != 0: #Can't divide by 0, nothing happens if numerator is 0
                if (dx / dy) == 1: #Slope, == 1 checks if the two coordinates make a diagonal
                    conflicts += 1
    return conflicts


def greedy_descent(assignment):
    """Takes an initial assignment to the n-queens problems and iteratively
       improves the assignment until a solution is found or a local minimum is
       reached
    """
    current_conflicts = conflict_count(assignment)
    current_assignment = assignment
    while (True):
        print("Assignment:", current_assignment, "Number of conflicts:", current_conflicts)
        
        if (current_conflicts == 0):
            print("A solution is found.")
            break        
        
        neighbour_conflicts = []
        for neighbour in neighbours(current_assignment):
            neighbour_conflicts.append((neighbour, conflict_count(neighbour)))
        neighbour_conflicts.sort()
            
        new_neighbour = ((), float('inf'))
        for neighbour in neighbour_conflicts:
            if neighbour[1] < current_conflicts and neighbour[1] < new_neighbour[1]:
                new_neighbour = neighbour
        
        if new_neighbour[1] == float('inf'):
            print("A local minimum is reached.")
            break
        
        current_assignment = new_neighbour[0]
        current_conflicts = new_neighbour[1]        



"""Write a function greedy_descent that takes an initial total assignment for the n-queens problem and iteratively improves the assignment until either a solution is found or a local minimum is reached. Like before, the assignment will be given in the form of a tuple. The assignment is a permutation of numbers from 1 to n. The value of n must be inferred from the given assignment. In order to implement this function you need to have implemented the functions in the previous two questions: neighbours and conflict_count.

In each iteration, the algorithm must print the current assignment and its corresponding number of conflicts. See the example. Use the print function in the following form to get the formatting right:

print("Assignment:", assignment, "Number of conflicts:", current_num_of_conflicts)
The function greedy_descent must consider all the neighbours of the current assignment and choose one that has the minimum number of conflicts and has fewer conflicts than the current assignment. If there is not such a neighbour, then a local minimum has been reached and the algorithm must report by the following print function (also see the examples):

print("A local minimum is reached.")
If an assignment (including the initial assignment) yields no conflict, then it is a solution and the algorithm must stop (after printing the assignment and the number of conflicts as above and) after printing a message using the following:

print("A solution is found.")
Important: When considering the neighbours of an assignment to choose the one with a minimum number of conflicts, if there is a tie, choose the assignment that comes first in the lexicographical ordering of tuples. For example when the current assignment is (1, 2, 3), its neighbours are [(2, 1, 3), (3, 2, 1), (1, 3, 2)] with the conflict counts of 1, 3, and 1 respectively. Thus there is tie between (2, 1, 3) and (1, 3, 2). The tie is broken by choosing (1, 3, 2) because it comes before (2, 1, 3). Note that this is not an essential part of the greedy descent algorithm. We are adding this condition only to be able to test the correctness of the output of an otherwise stochastic algorithm. One way of implementing this is to sort the neighbours before finding the one with the minimum number of conflicts.

Notes:

Consider using Python's min function with an appropriate 'key' function such that it behaves like an arg-min function. You can also add the required functionality regarding the ties (mentioned above) in this 'key' function. This is in fact a better solution than using sort (mentioned above) as the stability of Python's min is not documented in the language specification and therefore may vary in different implementations or versions of Python.
Your answer must include all the functions (and the import statements) that it depends on (e.g. functions neighbours and conflict_count)."""