import re


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
        
        
def forward_deduce(KB_str):
    """Takes a string of a knowledge base containg propositional definite
       clauses and returns a complete *set* of atoms (as strings) that can be
       derived (to be true) from the knowledge base.
    """
    clauses_list = list(clauses(KB_str))
    derived = set()
    derived_size = 0
    while True:
        for clause in clauses_list:
            valid = True
            for body_part in clause[1]:
                if not body_part in derived:
                    valid = False
            if valid:
                #print(clause[0])
                derived.add(clause[0])
        derived_size += 1
        if derived_size > len(derived): #If nothing has been added
            break
    
    #print(derived)
    return derived

def main():
    #Test case 1:
    kb = """
    a :- b.
    b.
    """
    
    print(", ".join(sorted(forward_deduce(kb))))
    
    #Test case 2:
    kb = """
    good_programmer :- correct_code.
    correct_code :- good_programmer.
    """
    
    print(", ".join(sorted(forward_deduce(kb))))
    
    #Test case 3:
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
    
    print(", ".join(sorted(forward_deduce(kb))))
    
if __name__ == "__main__":
    main()
