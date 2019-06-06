%listtran([Head|[]], [Trans|[]]) :- tran(Head, Trans).
listtran([], []).
listtran([Head|Tail], [Trans|Ttail]) :- tran(Head, Trans), listtran(Tail, Ttail).

tran(eins,one). 
tran(zwei,two). 
tran(drei,three). 
tran(vier,four). 
tran(fuenf,five). 
tran(sechs,six). 
tran(sieben,seven). 
tran(acht,eight). 
tran(neun,nine).

test_answer :-
    listtran([eins, neun, zwei], X),
    writeln(X).

test_answer2 :-
    listtran([], []),
    writeln('OK').

test_answer3 :-
    listtran(X, [one, seven, six, two]),
    writeln(X).

test_answer4 :-
    listtran(L1, L2),
    writeln('OK').

tran(1, one). 
tran(2, two). 
tran(3, three). 

test_answer5 :-
    listtran([1, 2, 3], X),
    writeln(X).
