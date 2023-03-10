class Commande:
    def __init__(self, date, numero, prix=0):
        self.date = date
        self.numero = numero
        self.prix = prix
        
    def get_date(self):
        return self.date
    
    def set_date(self, date):
        self.date = date
    
    def get_numero(self):
        return self.numero
    
    def set_numero(self, numero):
        self.numero = numero
    
    def get_prix(self):
        return self.prix
    
    def set_prix(self, prix):
        self.prix = prix
    
    def __str__(self):
        return f"Commande {self.numero} : {self.prix} €, passée le {self.date}"
    
    def acquitter(self):
        print(f"La commande {self.numero} a été acquittée.")
    
    def calculTVA(self):
        return self.prix * 0.196
    
    def __add__(self, other):
        max_num = max(int(self.numero), int(other.numero))
        new_num = str(max_num + 1)
        new_date = max(self.date, other.date)
        new_prix = self.prix + other.prix
        return Commande(new_date, new_num, new_prix)