num(A, B) :- A =:= B.

test(A, B) :- \+num(A, B).


test2 :- append([1, 2, 3], [4, 5, 6], X), writeln(X).


remove(X, [], []).
remove(X, [H1|T1], ListOut) :- X = H1, remove(X, T1, ListOut); remove(X, T1, Z), append([H1], Z, ListOut).

test_answer :-
    remove(a, [a, b, a, c, d, a, b], L),
    write(L),
    halt.

