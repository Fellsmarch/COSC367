merge2([], [], X, Result) :- Result = X.
merge2([Head1|Tail1], [Head2|Tail2], X, Result) :- Head1 =< Head2 -> merge2(Tail1, [Head2|Tail2], [Head1|X], Result) ; merge2([Head1|Tail1], Tail2, [Head2|X], Result).
%merge2([Head1|Tail1], [Head2|Tail2], X, Result) :- Head1 > Head2, merge2([Head1|Tail1], Tail2, [Head2|X], Result).

merge(List1, List2, X) :- merge2(List1, List2, [], X).


test_answer :-
    merge([3, 6, 7], [1, 2, 3, 5, 8], L),
    writeln(L).

test_answer2 :-
    merge([3, 6, 7], [], L),
    writeln(L).
