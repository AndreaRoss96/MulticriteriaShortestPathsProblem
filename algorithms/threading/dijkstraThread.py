"""
Per la soluzione con i thread per il mono criteria, si fa partire un thread dal target e uno dal source,
quando entrambi controllano un nodo già visitato viene costruito il percorso:
    - dalla source all'ultimo nodo visitato (source thread)
    - backtracking dall'ultimo modo visitato al target (target thread)

Per il bicriteria è poissibile applicare sicuramente l'algoritmo di binary search.
"""