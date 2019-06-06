reverse3([], Backward, Acc) :- Backward = Acc.
reverse3([Head|Tail], Backward, Acc) :- reverse3(Tail, Backward, [Head|Acc]).

reversed(Forward, Backward) :- reverse3(Forward, Backward, []).

test_answer :- 
    reversed([1, 2, 3, 4, 5], L),
    writeln(L).

test_answer2 :- 
    reversed(L, [d, c, b, a]),
    writeln(L).
