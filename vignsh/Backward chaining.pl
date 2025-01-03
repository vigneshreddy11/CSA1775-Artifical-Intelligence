% Facts
has_income(john, 50000).  % John has an income of 50,000
has_income(mary, 30000).  % Mary has an income of 30,000
has_age(john, 35).        % John is 35 years old
has_age(mary, 25).        % Mary is 25 years old

% Rules
eligible_for_loan(X) :-
    has_income(X, Income),
    Income >= 40000,         % Income should be greater than or equal to 40,000
    has_age(X, Age),
    Age >= 30.               % Age should be greater than or equal to 30

% Backward chaining process to check if a person is eligible for a loan
check_loan_eligibility(X) :-
    eligible_for_loan(X), !,    % Try to prove eligibility for a loan
    write(X), write(' is eligible for a loan.'), nl;
    write(X), write(' is not eligible for a loan.'), nl.
