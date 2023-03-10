from models.AB import AB

def lire_parcours_depuis_fichier(nom_fichier):
    with open(nom_fichier, 'r') as f:
        parcours = [int(x) for x in f.readline().strip().split()]
    return parcours
