addone([], []).
addone([Head1|Tail1], [Head2|Tail2]) :- Head2 is (Head1 + 1), addone(Tail1, Tail2).


test_answer :-
    addone([3, 6, 7], L),
    writeln(L).

test_answer2 :-
    addone([1, 2, 3, 4], [2, 3, 4, 5]),
    writeln('OK').
            
test_answer3 :-
    addone([], []),
    writeln('OK').
