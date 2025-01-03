% Facts: Symptoms associated with diseases
has_symptom(cold, cough).
has_symptom(cold, sneezing).
has_symptom(cold, fever).

has_symptom(flu, fever).
has_symptom(flu, headache).
has_symptom(flu, body_ache).

has_symptom(covid19, fever).
has_symptom(covid19, cough).
has_symptom(covid19, loss_of_taste_or_smell).
has_symptom(covid19, difficulty_breathing).

has_symptom(allergy, sneezing).
has_symptom(allergy, runny_nose).
has_symptom(allergy, itchy_eyes).

has_symptom(malaria, fever).
has_symptom(malaria, shivering).
has_symptom(malaria, sweating).
has_symptom(malaria, fatigue).

% Heuristic values: how likely the disease is based on the symptoms (lower = more likely)
heuristic(cold, 4).
heuristic(flu, 3).
heuristic(covid19, 2).
heuristic(allergy, 5).
heuristic(malaria, 6).

% Rule: Diagnosis based on symptoms
diagnose(Symptoms, Disease) :-
    findall(D, (has_symptom(D, Symptom), member(Symptom, Symptoms)), MatchedSymptoms),
    length(MatchedSymptoms, Matches),
    heuristic(Disease, H),
    assert(heuristic_value(Disease, Matches, H)).

% Best-First Search for diagnosis based on symptom matches and heuristics
best_first_search(Diseases, BestDiagnosis) :-
    findall((Disease, Matches, H), heuristic_value(Disease, Matches, H), Candidates),
    sort(3, @=<, Candidates, SortedCandidates),  % Sort by Matches and Heuristic value
    SortedCandidates = [(BestDiagnosis, _, _) | _],  % Choose the best diagnosis
    !.

% Query: Start the diagnosis process
start_diagnosis(Symptoms, Disease) :-
    retractall(heuristic_value(_, _, _)),  % Clear any previous diagnoses
    diagnose(Symptoms, _),  % Diagnose based on symptoms
    best_first_search(_, Disease),  % Choose the best diagnosis
    format('The best diagnosis is: ~w', [Disease]), nl.
