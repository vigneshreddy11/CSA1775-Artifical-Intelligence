% Facts
has_legs(dog).
has_legs(cat).
has_legs(human).
has_wings(eagle).
has_wings(parrot).
has_fur(dog).
has_fur(cat).

% Rules
is_mammal(X) :- has_legs(X), has_fur(X).  % Mammals have legs and fur
is_bird(X) :- has_wings(X).                % Birds have wings

% Backward chaining process to classify an animal
classify_animal(X) :-
    is_mammal(X), !,                        % Try to prove if it's a mammal
    write(X), write(' is a mammal.'), nl;
    is_bird(X), !,                          % If not a mammal, try to prove if it's a bird
    write(X), write(' is a bird.'), nl;
    write(X), write(' classification unknown.'), nl.  % If neither, output unknown
