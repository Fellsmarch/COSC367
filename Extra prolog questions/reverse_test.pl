reverse2(List, Output):- reverse(List, Output).

	
test_answer :- reverse2([0, b, 1, 0, 1], X),
               writeln(X).
