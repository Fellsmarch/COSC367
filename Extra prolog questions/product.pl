product([], 1).
product([Head|[]], Head).
product([Head|Tail], Product) :- product(Tail, NewProduct), Product is NewProduct * Head.


test_answer :- product([1, 2, 3], X), 
               writeln(X).

test_answer2 :- product([], X),
               writeln(X).
