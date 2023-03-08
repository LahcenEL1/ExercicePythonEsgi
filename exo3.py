nb = float(input("Entre la pression actuelle: "))
if nb >=0:
    racine = nb **0.5
    print('La racine carre de {} est {:.2f}'.format(nb,racine))
else:
    print('Erreur : le nb doit etre positif ou nul')