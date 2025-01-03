% Facts: These represent the relationship between symptoms and diseases.
has_symptom(john, fever).
has_symptom(john, cough).
has_symptom(john, sore_throat).

has_symptom(mary, headache).
has_symptom(mary, nausea).
has_symptom(mary, fever).

has_symptom(susan, fatigue).
has_symptom(susan, cough).
has_symptom(susan, shortness_of_breath).

% Rules: These define which diseases are associated with a set of symptoms.

% Disease 1: Flu
diagnosis(john, flu) :-
    has_symptom(john, fever),
    has_symptom(john, cough),
    has_symptom(john, sore_throat).

% Disease 2: Cold
diagnosis(susan, cold) :-
    has_symptom(susan, cough),
    has_symptom(susan, fatigue).

% Disease 3: COVID-19
diagnosis(susan, covid19) :-
    has_symptom(susan, fatigue),
    has_symptom(susan, shortness_of_breath),
    has_symptom(susan, cough).

% Disease 4: Malaria
diagnosis(mary, malaria) :-
    has_symptom(mary, fever),
    has_symptom(mary, headache),
    has_symptom(mary, nausea).

% Query example:
% To diagnose john, you would query: diagnosis(john, Disease).
