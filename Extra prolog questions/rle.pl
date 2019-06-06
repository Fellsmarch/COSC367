getCount(Char, Num, [], Tuple) :- Tuple = (Char, Num).
getCount(Char, OldNum, [NewChar|Input], Tuple) :- Char = NewChar, NewNum is OldNum + 1, getCount(Char, NewNum, Input, Tuple); getCount(Char, OldNum, Input, Tuple). 

rle2([], Output, Added, X) :- X = Output.
rle2([Char|Input], OldOutput, Added, X) :- \+member(Char, Added), 
                                        getCount(Char, 1, Input, Tuple), 
                                        append(OldOutput, [Tuple], NewOutput), 
                                        rle2(Input, NewOutput, [Char|Added], X)
                                        ; 
                                        rle2(Input, OldOutput, Added, X).

rle(Input, Output) :- rle2(Input, [], [], Output).

test_answer :- rle([a, a, b, c, c, c], X),
               writeln(X).
