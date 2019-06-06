binary_number([0, b|[0|[]]]).
binary_number([0, b|[1|Tail]]) :- one_or_zero(Tail).
one_or_zero([]).
one_or_zero([Head|Tail]) :- (Head is 0; Head is 1), one_or_zero(Tail).


test_answer :- binary_number([0, b, 1, 0, 1]), 
               writeln('OK').

test_answer2 :- binary_number([0, b, 0, 1]), 
               writeln('Wrong'), halt.
test_answer2 :- writeln('OK').
