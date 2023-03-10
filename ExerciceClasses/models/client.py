class Client:
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse
        
    def get_nom(self):
        return self.nom
    
    def set_nom(self, nom):
        self.nom = nom
    
    def get_adresse(self):
        return self.adresse
    
    def set_adresse(self, adresse):
        self.adresse = adresse
    
    def __str__(self):
        return f"Client : {self.nom}, {self.adresse}"
    
    def contacter(self):
        return f"Le client {self.nom} peut être contacté à l'adresse {self.adresse}."
