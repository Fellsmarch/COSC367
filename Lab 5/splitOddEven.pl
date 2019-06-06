%Naive method without using modulus
reverse([],L,L).
reverse([Head|Tail], Accu, Rev) :- reverse(Tail, [Head|Accu], Rev).

%Using 1 or 0 to represent odd or even
splitOddEven([], OddList, EvenList, Odd, Even, _) :- reverse(OddList, [], Odd), reverse(EvenList, [], Even).
splitOddEven([Head|Input], OddList, EvenList, Odd, Even, 0) :- splitOddEven(Input, OddList, [Head|EvenList], Odd, Even, 1).
splitOddEven([Head|Input], OddList, EvenList, Odd, Even, 1) :- splitOddEven(Input, [Head|OddList], EvenList, Odd, Even, 0).

split_odd_even([Head|Input], Odd, Even) :- splitOddEven(Input, [Head|[]], [], Odd, Even, 0).
split_odd_even([], [], []).




test_answer :-
    split_odd_even([a,b,c,d,e,f,g], A, B),
    write(A),
    writeln(B).

test_answer2 :-
    split_odd_even([1,2,3,5], A, B),
    write(A),
    writeln(B).

test_answer3 :-
    split_odd_even([d], A, B),
    write(A),
    writeln(B).

test_answer4 :-
    split_odd_even([], A, B),
    write(A),
    writeln(B).


/*splitEven([], OddList, EvenList, Odd, Even) :- reverse(OddList, [], Odd), reverse(EvenList, [], Even).
splitEven([Head|Input], OddList, EvenList, Odd, Even) :- splitOdd(Input, OddList, [Head|EvenList], Odd, Even).

splitOdd([], OddList, EvenList, Odd, Even) :- reverse(OddList, [], Odd), reverse(EvenList, [], Even).
splitOdd([Head|Input], OddList, EvenList, Odd, Even) :- splitEven(Input, [Head|OddList], EvenList, Odd, Even).

split_odd_even([Head|Input], Odd, Even) :- splitEven(Input, [Head|[]], [], Odd, Even).*/

split_odd_even([], [], []).
split_odd_even([X], [X], []).

split_odd_even([A, B | T], [A | Odds], [B | Evens] ) :- split_odd_even(T, Odds, Evens).
