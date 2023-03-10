class Player:
    def __init__(self, pseudo, health, attack) :
        self.pseudo = pseudo
        self.health = health
        self.attack = attack

    def get_pseudo(self):
        return self.pseudo
    def get_health(self):
        return self.health
    
player1 = Player("Test",10,10)

print("Bienvenue au joueur",player1.pseudo)