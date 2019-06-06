valAtPos([Value|_], Index, Value, Index).
valAtPos([_|Tail], Index, Value, OldCurrent) :- NewCurrent is OldCurrent + 1, valAtPos(Tail, Index, Value, NewCurrent).

element(List, Index, Value) :- valAtPos(List, Index, Value, 0).

test_answer :-
    element([a, b, c, d, e, f], 2, X),
    writeln(X).

test_answer2 :-
    element([a, b, c, d], I, d),
    writeln(I).

test_answer3 :-
    element([a, b, c, d], 6, X),
    writeln('Wrong answer!').
    
test_answer3 :-
    writeln('OK').

test_answer4 :-
    element(L, I, X),
    writeln('OK').
