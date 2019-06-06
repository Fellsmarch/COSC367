postorder(leaf(Label), [Traversal]) :- Traversal = Label.
postorder(tree(Root, Left_subtree, Right_subtree), Traversal) :- postorder(Left_subtree, LTraversal), postorder(Right_subtree, RTraversal), append(LTraversal, RTraversal, Traversal2), append(Traversal2, [Root], Traversal).


test_answer :- postorder(tree(a, leaf(b), leaf(c)), T), writeln(T).

test_answer2 :- postorder(tree(a, tree(b, leaf(c), leaf(d)), leaf(e)), T),
               writeln(T).
