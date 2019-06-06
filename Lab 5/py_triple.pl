py_triple(A, B, C) :- 0 < A, A =< B, B =< C, C_s is (C * C), C_s is ((A * A) + (B * B)).

test_answer :-
    py_triple(3,4,5),
    write('OK').
