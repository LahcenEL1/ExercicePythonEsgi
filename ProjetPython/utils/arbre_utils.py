from models.AB import AB

def construire_arbre(parcours, type_parcours='prefixe'):
    if type_parcours == 'prefixe':
        racine = parcours[0]
        index = 1
        while index < len(parcours) and parcours[index] < racine:
            index += 1
        if index == len(parcours):
            gauche = None
            droite = None
        else:
            gauche = construire_arbre(parcours[1:index], type_parcours)
            droite = construire_arbre(parcours[index:], type_parcours)
    elif type_parcours == 'infixe':
        index = len(parcours) // 2
        racine = parcours[index]
        if index == 0:
            gauche = None
        else:
            gauche = construire_arbre(parcours[:index], type_parcours)
        if index == len(parcours) - 1:
            droite = None
        else:
            droite = construire_arbre(parcours[index+1:], type_parcours)
    elif type_parcours == 'postfixe':
        racine = parcours[-1]
        index = -2
        while index >= -len(parcours) and parcours[index] > racine:
            index -= 1
        if index == -len(parcours) - 1:
            gauche = None
            droite = None
        else:
            droite = construire_arbre(parcours[index+1:-1], type_parcours)
            gauche = construire_arbre(parcours[:index+1], type_parcours)
    else:
        raise ValueError('Type de parcours invalide')
    
    return AB(racine, gauche, droite)