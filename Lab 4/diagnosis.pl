/* tear rate related clauses */
normal_tear_rate(RATE) :- RATE >= 5.
low_tear_rate(RATE) :- RATE < 5.

/* age-related clauses */
young(AGE) :- AGE < 45.

diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :- Recommend = hard_lenses, young(Age), Astigmatic = yes, normal_tear_rate(Tear_Rate).
diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :- Recommend = soft_lenses, young(Age), Astigmatic = no, normal_tear_rate(Tear_Rate).
diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :- Recommend = no_lenses, low_tear_rate(Tear_Rate).

/* Tests */
test_answer1 :-
    diagnosis(hard_lenses, 21, yes, 11),
    writeln('OK').

test_answer2 :-
    diagnosis(X, 45, no, 4),
    writeln(X).

test_answer3 :-
    diagnosis(X, 19, no, 5),
    writeln(X). 
