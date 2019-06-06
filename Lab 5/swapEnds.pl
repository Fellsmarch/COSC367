%getLast([Last|[]], Last).
%getLast([_|Tail], Last) :- getLast(Tail, Last).
%
%swap_ends([Head1|Tail1], [Head2|Tail2]) :- getLast(Tail1, Last1), getLast(Tail2, Last2), Head1 == Last2, Head2 == Last1.

swapEnds([Head2|[]], [Head1|[]], Head1, Head2).
swapEnds([Head|Tail1], [Head|Tail2], Head1, Head2) :- swapEnds(Tail1, Tail2, Head1, Head2).

swap_ends([Head1|Tail1], [Head2|Tail2]) :- swapEnds(Tail1, Tail2, Head1, Head2).

test_answer :-
    swap_ends([a, b, c, d, e, f], L),
    writeln(L).

test_answer2 :-
    swap_ends(L1, L2),
    writeln('OK').

test_answer3 :-
    swap_ends(L, [term1, term2, term3, term4]),
    writeln(L).

test_answer4 :-
    swap_ends([367], L),
    writeln('Wrong answer!').
    
test_answer4 :-
    writeln('OK').
               
