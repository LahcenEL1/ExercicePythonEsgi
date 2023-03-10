from models.AB import AB
from utils.arbre_utils import construire_arbre
from utils.lecture_utils import lire_parcours_depuis_fichier

# # Création d'un arbre binaire avec racine 1, gauche 2 et droite 3
# arbre = AB(1, AB(2), AB(3))

# # Affichage des valeurs des attributs de l'arbre
# print(arbre.get_racine())  # 1
# print(arbre.get_gauche().get_racine())  # 2
# print(arbre.get_droite().get_racine())  # 3

# # Vérification si l'arbre est vide ou non
# print(arbre.estVide())  # False

# # Création d'un arbre binaire vide
# arbre_vide = AB()

# # Vérification si l'arbre est vide ou non
# print(arbre_vide.estVide())  # True


# 3. Création de l'arbre vide A1 et test de estVide()
A1 = AB()
print(A1.estVide())  # True

# 4. Création de l'arbre A2 avec une racine de valeur 5 et test de estVide()
A2 = AB(5)
print(A2.estVide())  # False

# 5. Création de l'arbre A3 avec une racine de valeur 3
A3 = AB(3)

# 6. Modification de la partie gauche de A2 pour y placer A3
A2.set_gauche(A3)

# 7. Création de l'arbre Atest
Atest = AB(10, AB(5, AB(3), AB(8)), AB(12))

# Test de estVide()
print(Atest.estVide())  # False


# Test de la méthode taille()
print(Atest.taille())  # 5

# Test de la méthode prefixe()
print("Le parcours prefixe est   ")
print(Atest.prefixe())  # affiche 10 5 3 8 12


# Test de la méthode infixe()
print("Le parcours infixe est   ")
print(Atest.infixe())  # affiche 3 5 8 10 12 


# Test de la méthode postfixe()
print("Le parcours postfixe est   ")
print(Atest.postfixe())  # affiche 3 8 5 12 10


# Test de la méthode hauteur()
print("La hauteur de Atest est de :", Atest.hauteur())

# Test de la méthode estABR()
print("Atest est un ABR :", Atest.estABR())

# Test de la méthode estEquilibre()
print("Atest est équilibré :", Atest.estEquilibre())


parcours_prefixe = lire_parcours_depuis_fichier('parcours_prefixe.txt')
parcours_infixe = lire_parcours_depuis_fichier('parcours_infixe.txt')
parcours_postfixe = lire_parcours_depuis_fichier('parcours_postfixe.txt')

arbre_prefixe = construire_arbre(parcours_prefixe, 'prefixe')
arbre_infixe = construire_arbre(parcours_infixe, 'infixe')
arbre_postfixe = construire_arbre(parcours_postfixe, 'postfixe')


# Test de la lecture du prefixe
print("Test de la lecture prefixe  :")
arbre_prefixe.prefixe()

# Test de la lecture du postfixe
print("Test de la lecture postfixe  :")
arbre_prefixe.postfixe()


# Test de la lecture du infixe
print("Test de la lecture infixe  :")
arbre_prefixe.infixe()









# Test pour le DS
a = 15 
b = 'moutons'
c = 32
d ='vaches'
e = 15
f = 'poules'

print ("J'ai %i %s, %i %s et %i %s"%(c,b,e,f,a,PendingDeprecationWarning))

i = 0
j = 5
k = 2
print (range(i,j,k))

def ope1 (a,b,c):
    return a+b*c

def ope2 (a,b,c):
    return a*2+b

def ope3 (a,b,c):
    return c*3-b

i = 2
j = 2
k = 3

if i > 5:
    resultat = ope1(1, j, k)
elif j < 3:
    resultat = ope2 (j, k, i)
else:
    resultat = ope3 (k, j, i)
print (resultat)