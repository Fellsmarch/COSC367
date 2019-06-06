import re
from search import *

def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    Author: Kourosh Neshatian
    Last Modified: 31 Jul 2018

    """
    ATOM   = r"[a-z][a-zA-z\d_]*"
    HEAD   = f"\\s*(?P<HEAD>{ATOM})\\s*"
    BODY   = f"\\s*(?P<BODY>{ATOM}\\s*(,\\s*{ATOM}\\s*)*)\\s*"
    CLAUSE = f"{HEAD}(:-{BODY})?\\."
    KB     = f"^({CLAUSE})*\\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")
        
        
class KBGraph(Graph):
    """"""
    def __init__(self, knowledge_base, query):
        """Initialises a KBGraph
        Keyword Arguments:
        knowledge_base -- The knowledged base we are working with
        query -- The query to test??
        """
        
        self.clauses_list = list(clauses(knowledge_base))
        self.query = query
    
    def is_goal(self, node):
        """Returns true if the given node is a goal state, false otherwise."""
        return len(node) == 0

    def starting_nodes(self):
        """Returns a sequence of starting nodes. Often there is only one
        starting node but even then the function returns a sequence
        with one element. It can be implemented as an iterator if
        needed.
        """
        yield self.query

    def outgoing_arcs(self, tail_node):
        """Given a node it returns a sequence of arcs (Arc objects)
        which correspond to the actions that can be taken in that
        state (node)."""
        tail_list = list(tail_node)
        for clause in self.clauses_list:
            if clause[0] == tail_list[0]:
                head = clause[1]
                yield Arc(tail_node, head, str(tail_node) + '->' + str(head), 0)

    
        
        
class DFSFrontier(Frontier): #From Quiz 1
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty list."""
        self.container = []


    def add(self, path):
        self.container.append(path) #Maybe add to start

    def __iter__(self):
        while len(self.container) > 0:
            yield self.container.pop()
            
            
class BFSFrontier(Frontier): #From Quiz 1
    """Implements a frontier container appropriate for breadth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty list."""
        self.container = []


    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        while len(self.container) > 0:
            yield self.container.pop(0)
            
            
def main():
    #Test case 1:
    kb = """
    a :- b, c.
    b :- d, e.
    b :- g, e.
    c :- e.
    d.
    e.
    f :- a,
         g.
    """
    
    query = {'a'}
    if next(generic_search(KBGraph(kb, query), BFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")    
    
    #Test case 2:
    kb = """
    a :- b, c.
    b :- d, e.
    b :- g, e.
    c :- e.
    d.
    e.
    f :- a,
         g.
    """
    
    query = {'a', 'b', 'd'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")    
    
    #Test case 3:
    kb = """
    all_tests_passed :- program_is_correct.
    all_tests_passed.
    """
    
    query = {'program_is_correct'}
    if next(generic_search(KBGraph(kb, query), BFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")    
    
    #Test case 4: 
    kb = """
    a :- b.
    """
    
    query = {'c'}
    if next(generic_search(KBGraph(kb, query), BFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")
        
        
if __name__ == "__main__":
    main()