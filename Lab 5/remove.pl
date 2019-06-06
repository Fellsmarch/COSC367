remove(_, [], []).
remove(ToRemove, [ToRemove|Tail], Result) :- remove(ToRemove, Tail, Result).
remove(ToRemove, [Head|Tail], Result) :- ToRemove \= Head, remove(ToRemove, Tail, [Head|Result]).


test_answer :- 
    remove(1, [1,2,1,4,3,3], Result),
    writeln(Result).
