fibfull(2, List, Output) :- reverse(List, Output).
fibfull(3, [Last1, Last2|List], Output) :- Y is Last1 + Last2, reverse([Y, Last1, Last2|List], Output).
fibfull(N, [Last1, Last2|List], Output) :- N > 3, Y is Last1 + Last2, Z is N - 1, fibfull(Z, [Y, Last1, Last2|List], Output).

fib(N, X) :- fibfull(N, [1, 0], X).


test_answer :- fib(2, [0, 1]),
               writeln('OK').

test_answer2 :- fib(6, X),
               writeln(X).
