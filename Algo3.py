def tri_rapide(tableau):
    if len(tableau) <= 1:
        return tableau
    pivot = tableau[len(tableau)//2]
    gauche = [x for x in tableau if x < pivot]
    milieu = [x for x in tableau if x == pivot]
    droite = [x for x in tableau if x > pivot]
    return tri_rapide(gauche) + milieu + tri_rapide(droite)
