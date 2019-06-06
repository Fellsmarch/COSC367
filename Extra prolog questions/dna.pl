dna([], []).
dna([c|Tail], [g|Tail2]) :- dna(Tail, Tail2).
dna([g|Tail], [c|Tail2]) :- dna(Tail, Tail2).
dna([a|Tail], [t|Tail2]) :- dna(Tail, Tail2).
dna([t|Tail], [a|Tail2]) :- dna(Tail, Tail2).

test_answer :- dna([a, t, c, g], X),
               writeln(X).

test_answer2 :- dna(X, [t, a, g, c]),
               writeln(X).
