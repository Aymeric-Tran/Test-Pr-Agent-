def tri_selection(tableau):
    for i in range(len(tableau)):
        mini = i
        for j in range(i+1, len(tableau)):
            if tableau[j] < tableau[mini]:
                mini = j
        # On échange les éléments            
        tableau[mini], tableau[i] = tableau[i], tableau[mini]
    return tableau
