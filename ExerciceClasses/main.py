from models.commande import Commande
from models.client import Client


commande1 = Commande("21/02/01","0781307996")

print("La commande est ", commande1.get_prix())

# Création de deux instances de la classe Commande
cmd1 = Commande("2022-02-14", "001", 20.0)
cmd2 = Commande("2022-02-15", "002", 30.0)

# Ajout des deux instances de la classe Commande avec la méthode __add__
cmd3 = cmd1 + cmd2

# Affichage des instances de la classe Commande
print(cmd1)
print(cmd2)
print(cmd3)