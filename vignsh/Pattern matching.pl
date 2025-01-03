% Base case: A single-element list has the same first and last element.
match_first_last([X], X).

% General case: Match the first and last elements of a list.
match_first_last([First | Tail], Last) :-
    append(_, [Last], Tail),  % Find the last element in the list
    format('First element: ~w, Last element: ~w~n', [First, Last]).

