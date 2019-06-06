py_triple(A, B, C, Min, Max) :- 0 < A, A =< B, B =< C, C_s is (C * C), C_s is ((A * A) + (B * B)), A >= Min, B >= Min, C >= Min, A =< Max, B =< Max, C =< Max.

test_answer :-
    findall([A,B,C],py_triple(A,B,C,1,10),List),
    writeln(List).
