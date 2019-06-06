reflection(point(X, Y), point(Y, X)).

test_answer1 :-
	reflection(point(3, 6), point(6, 3)),
        writeln('OK').

test_answer2 :-
	reflection(point(-5, 8), point(X, Y)),
        writeln(point(X, Y)).
