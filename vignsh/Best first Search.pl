% Facts: Node connections with associated costs (edge).
edge(a, b, 1).
edge(b, c, 1).
edge(a, c, 3).
edge(c, d, 1).
edge(b, d, 4).

% Heuristic values for each node (estimated cost to reach goal).
heuristic(a, 4).
heuristic(b, 3).
heuristic(c, 1).
heuristic(d, 0).  % Goal node (d) has a heuristic of 0.

% Best-First Search Algorithm
best_first_search(Start, Goal, Path, Cost) :-
    best_first_search([Start], [], Goal, Path, 0, Cost).

best_first_search([Goal | Rest], _, Goal, [Goal | Rest], Cost, Cost).
best_first_search([Current | Rest], Visited, Goal, Path, AccumulatedCost, TotalCost) :-
    findall(Next, (edge(Current, Next, _), \+ member(Next, Visited)), Neighbors),
    best_first_search_expand(Neighbors, [Current | Visited], Goal, Rest, NeighborsWithCosts),
    sort(2, @=<, NeighborsWithCosts, SortedNeighbors),
    SortedNeighbors = [(Next, EdgeCost) | _],
    NewCost is AccumulatedCost + EdgeCost,
    best_first_search([Next | Rest], [Current | Visited], Goal, Path, NewCost, TotalCost).

% Expand neighbors and add their heuristic values.
best_first_search_expand([], _, _, [], []).
best_first_search_expand([Next | Rest], Visited, Goal, RestExpanded, [(Next, Cost) | ExpandedRest]) :-
    edge(Current, Next, Cost),
    heuristic(Next, H),
    TotalCost is Cost + H,
    best_first_search_expand(Rest, Visited, Goal, RestExpanded, ExpandedRest).

% Query to start the Best-First Search.
