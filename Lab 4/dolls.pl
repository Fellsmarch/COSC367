directlyIn(olga, katarina).
directlyIn(natasha, olga).
directlyIn(irina, natasha).

contains(Doll1, Doll2) :- directlyIn(X, Doll1), contains(X, Doll2).
contains(Doll1, Doll2) :- directlyIn(Doll2, Doll1).

/* Test */
test_answer1 :-
    directlyIn(irina, natasha),
    writeln('OK').

test_answer2 :-
    \+ directlyIn(irina, olga),
    writeln('OK').

test_answer3 :-
    contains(katarina, irina),
    writeln('OK').

test_answer4 :-
    contains(katarina, natasha),
    writeln('OK').
