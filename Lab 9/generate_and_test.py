from csp import *
import itertools

def generate_and_test(csp):
    names, domains = zip(*csp.var_domains.items())
    for values in itertools.product(*domains):
        assignment = {x:v for x, v in zip(names, values)}
        #print(assignment)
        if all([satisfies(assignment, constraint) for constraint in csp.constraints]):
            yield assignment
            
