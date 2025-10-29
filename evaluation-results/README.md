# Evaluation results

This folder contains the results for four different research questions:

**RQ1 (Feasibility):** Is the planning problem generator able to create (JSON formatted) planner inputs correctly? To validate that the generator produces outputs that are not only syntactically compliant with the required JSON format but are also semantically valid, yielding solvable planning problems.

**RQ2 (Adaptation):** How effective is our approach in dealing with monitored changes by adapting the generated explanation? To assess COMPASS end-to-end ability to dynamically reconfigure explanations based on monitored changes on user interactions, shifts in cognitive state and acceptance rates.

**RQ3 (Alignment):** How well do the generated explanations align with the prompt? How well is a new adapted explanation based on user’s feedback perceived? To evaluate the controllability of the generator and the subjective quality of its output from a human perspective. We evaluate the system’s fidelity in adhering to explicit constraints like tone, format, and detail. Then, we evaluate user perception of adapted explanations to determine if the changes are seen as improvements.

**RQ4 (Personalisation):** How well are the explanation generator in tailoring the explanations to different user profiles? To ensure that the system can produce different tailored explanations for a diverse range of user profiles.
