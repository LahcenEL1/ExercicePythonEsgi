class CommandeAcquittee(Commande):
    def __init__(self, date, numero, prix=0, date_paiement=None):
        super().__init__(date, numero, prix)
        self.date_paiement = date_paiement
        
    def get_date_paiement(self):
        return self.date_paiement
    
    def set_date_paiement(self, date_paiement):
        self.date_paiement = date_paiement
    
    def __str__(self):
        if self.date_paiement is not None:
            return f"Commande {self.numero} : {self.prix} €, passée le {self.date}, acquittée le {self.date_paiement}"
        else:
            return super().__str__()