import itertools, copy 
from csp import *

def generate_and_test(csp):
    names, domains = zip(*csp.var_domains.items())
    for values in itertools.product(*domains):
        assignment = {x:v for x, v in zip(names, values)}
        #print(assignment)
        if all([satisfies(assignment, constraint) for constraint in csp.constraints]):
            yield assignment
            
def arc_consistent(csp):
    csp = copy.deepcopy(csp)
    tda = {(x, c) for c in csp.constraints for x in scope(c)}
    while tda:
        x, c = tda.pop()
        ys = list(scope(c) - {x})
        new_domain = set()
        for xval in csp.var_domains[x]:
            assignment = {x: xval}
            for yvals in itertools.product(*[csp.var_domains[y] for y in ys]):
                assignment.update({y: yval for y, yval in zip(ys, yvals)})
                if satisfies(assignment, c):
                    new_domain.add(xval)
                    break
        if csp.var_domains[x] != new_domain:
            csp.var_domains[x] = new_domain
            for cprime in set(csp.constraints) - {c}:
                if x in scope(cprime):
                    for z in scope(cprime):
                        if x != z:
                            tda.add((z, cprime))
    return csp


"""This represents the following cryptarithmetic problem. Wherein each
   letter represents a digit. Each digit is associated with a maximum of one
   letter and each letter with exactly one digit. The letters on the left 
   cannot be zero. The problem:
      two
   +  two
   ------
     four"""
cryptic_puzzle = CSP(
    var_domains = {x: set(range(0, 10)) for x in 'twofur'},
    constraints = {
        lambda t, w, o, f, u, r: len([t, w, o, f, u, r]) == len(set([t, w, o, f, u, r])),
        lambda o, r: (o + o) % 10 == r,      
        lambda w, u, o: (w + w + ((o + o) // 10)) % 10 == u,
        lambda t, o, w: (t + t + ((w + w) // 10)) % 10 == o, #Don't need to worry about o+o as it wouldn't make a difference (5 + 5) // 10 = 1 & (4 + (4 + 1)) // 10 == 0
        lambda t: t >= 5, #since f has to be 1, t must carry over
        lambda f: f == 1, #since it can't be zero and no three digit numbers added together can equal over 1 in the fourth digit
        
    })
    
    
    
    