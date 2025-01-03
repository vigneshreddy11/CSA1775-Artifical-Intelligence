% Define some facts
animal(dog).
animal(cat).
animal(elephant).
animal(lion).

% Define a rule that checks if an animal is a mammal
mammal(X) :-
    animal(X),
    (X == dog; X == cat; X == elephant; X == lion).

% Rule to check if a list contains a particular element
contains([Head | _], Head).  % The element is at the head of the list
contains([_ | Tail], X) :-   % Recursively search the tail of the list
    contains(Tail, X).

% Pattern matching on a list (e.g., to find if a particular pattern exists)
find_pattern([], []).
find_pattern([Head1 | Tail1], [Head2 | Tail2]) :-
    Head1 == Head2,          % Match the current element
    find_pattern(Tail1, Tail2). % Continue matching the rest of the list
