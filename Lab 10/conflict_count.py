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


"""Write a function conflict_count that takes a total assignment for an n-queen problem and returns the number conflicts for that assignment. We define the number of conflicts to be the number of unordered pairs of queens (objects) that threaten (attack) each other. The assignment will be given in the form of a sequence (tuple more specifically). The assignment is a permutation of numbers from 1 to n. The value of n must be inferred from the given assignment.

Hint: diagonals have a slope of 1 or -1. You want to see if abs(dx)==abs(dy)."""