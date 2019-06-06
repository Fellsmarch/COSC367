swap12([X, Y|Tail], [Y, X|Tail]).

test_answer :-
    swap12([a, b, c, d], L),
    writeln(L).

test_answer2 :-
    \+ swap12(L, [1]),
    writeln('OK').

test_answer3 :-
    swap12(L, [b, a]),
    writeln(L).

test_answer4 :-
    swap12(L1, L2),
    writeln('OK').


%swap12(?List1, ?List2) = true if List1 == List2, except List1[0] & List2[0] are swapped. Always fails with lists with length < 2


