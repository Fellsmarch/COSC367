second([_, X | _], X).

test_answer :-
    second([cosc, 2, Var, beethoven], X),
    writeln(X).

test_answer2 :-
    \+ second([1], X),
    writeln('OK').

test_answer3 :-
    second([a, b, c, d], b),
    writeln('OK').

test_answer4 :-
    second(L, X),
    writeln('OK').

%? Means that either of the arguments can be instantiated or unbound (they can be input or output)
