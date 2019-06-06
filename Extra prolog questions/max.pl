max([], Max).
max([Head|Tail], Max) :- Max > Head, max(Tail, Max).


test_answer :- 
    max([1, 2, 3, 4, 5], M),
    writeln(M).

test_answer2 :- 
    max([], M),
    writeln("Max of an empty list is undefined!").

