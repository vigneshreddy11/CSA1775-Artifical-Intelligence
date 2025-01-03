% Define the vowels
vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).

% Base case: An empty list or string has 0 vowels.
count_vowels([], 0).

% Recursive case: If the head of the list is a vowel, increment the count.
count_vowels([Head | Tail], Count) :-
    vowel(Head),            % Check if the head is a vowel
    count_vowels(Tail, TailCount),  % Count vowels in the tail
    Count is TailCount + 1.         % Add 1 to the count

% Recursive case: If the head of the list is not a vowel, continue with the tail.
count_vowels([Head | Tail], Count) :-
    \+ vowel(Head),         % Check if the head is not a vowel
    count_vowels(Tail, Count).  % Continue with the tail

% Wrapper to count vowels in a string
count_vowels_in_string(String, Count) :-
    string_chars(String, CharList),  % Convert string to list of characters
    count_vowels(CharList, Count).   % Count vowels in the character list
