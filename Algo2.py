def tri_insertion(tableau):
    for i in range(1, len(tableau)):
        en_cours = tableau[i]
        j = i
        while j > 0 and tableau[j-1] > en_cours:
            tableau[j] = tableau[j-1]
            j -= 1
        tableau[j] = en_cours
    return tableau
