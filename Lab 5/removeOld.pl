reverse([],L,L).
reverse([Head|Tail], Accu, Rev) :- reverse(Tail, [Head|Accu], Rev).

removeAll(_, [], Result, Acc) :- reverse(Acc, [], Reversed), Result = Reversed.
removeAll(ToRemove, [ToRemove|Tail], Result, Acc) :- removeAll(ToRemove, Tail, Result, Acc).
removeAll(ToRemove, [Head|Tail], Result, Acc) :- removeAll(ToRemove, Tail, Result, [Head|Acc]).
%How do I make this not a reversed list

remove(ToRemove, Input, Result) :- removeAll(ToRemove, Input, Result, []).

test_answer :-
    remove(a, [a, b, a, c, d, a, b], L),
    writeln(L).

test_answer2 :-
    remove(2, [2], L),
    writeln(L).

test_answer3 :-
    remove(d, [a, b, c], L),
    write(L).

test_answer4 :-
    remove(a, [], L),
    write(L).

test_answer5 :-
    remove(term2, [term1, term2, term3], [term1, term3]),
    write('OK').
