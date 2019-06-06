new_append([], List2, List2).
new_append([Head|Tail], List2, [Head|Output]) :- new_append(Tail, List2, Output).

test_answer :-
    new_append([1, 2, 3], [a, b, c], L),
    writeln(L).

test_answer2 :-
    new_append([1, 2, 3], L, [1, 2, 3, 4, 5]),
    writeln(L).
