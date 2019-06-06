preorder(leaf(Label), [Traversal]) :- Traversal = Label.
preorder(tree(Root, Left_subtree, Right_subtree), [Root|Traversal]) :- preorder(Left_subtree, LTraversal), preorder(Right_subtree, RTraversal), append(LTraversal, RTraversal, Traversal).


test_answer :- preorder(leaf(a), L), 
               writeln(L).

test_answer2 :- preorder(tree(a, tree(b, leaf(c), leaf(d)), leaf(e)), T), 
               writeln(T).
