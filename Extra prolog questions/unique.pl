unique([], Set) :
unique([Head|Tail], [Head|Set]) :- \+ member(Head, Set), unique(Tail, Set). %Rebuilding on EXIT not on call
unique([Head|Tail], Set) :- member(Head, Set), unique(Tail, Set).



test_answer :- 
    unique([1,2,1,4,3,3], Set),
    sort(Set,Sorted),
    writeln(Sorted).

test_answer2 :- 
    unique([], Set),
    sort(Set,Sorted),
    writeln(Sorted).

test_answer3 :-
    unique([8,8,8], X),
    writeln(X).
