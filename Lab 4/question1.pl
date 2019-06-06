eats(Person, Food) :- likes(Person, Food).
eats(Person, Food) :- hungry(Person), edible(Food).
