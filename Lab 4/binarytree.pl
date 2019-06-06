mirror(leaf(Label), leaf(Label)).
mirror(tree(B1, B2), tree(B3, B4)) :- mirror(B2, B3), mirror(B1, B4).

/* Tests */
test_answer1 :-
    mirror(leaf(foo), leaf(foo)),
    write('OK').
   


test_answer2 :-
    mirror(tree(leaf(foo), leaf(bar)), tree(leaf(bar), leaf(foo))),
    write('OK').
    


test_answer3 :-
    mirror(tree(tree(leaf(1),  leaf(2)),  leaf(4)), T),
    write(T).
    


test_answer4 :-
    mirror(tree(tree(leaf(1),  leaf(2)),  tree(leaf(3), leaf(4))), T),
    write(T).
   

