inside(Min, Max, X) :- Min =< Max, X is Min.
inside(OldMin, Max, X) :- NewMin is (OldMin + 1), NewMin =< Max, inside(NewMin, Max, X). %Since it will call both functions everytime since they are both valid.

test_answer :-
    inside(1,3,2),
    writeln('OK').

test_answer2 :-
    findall(X, inside(1, 3, X), List),
    writeln(List).

test_answer3 :-
    findall(X, inside(1, -1, X), List),
    writeln(List).
