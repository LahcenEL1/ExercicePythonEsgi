class AB:
    def __init__(self, racine=None, gauche=None, droite=None):
        if racine is None:
            self.racine = [None]
        else:
            self.racine = [racine]
        self.gauche = gauche
        self.droite = droite
    
    def set_racine(self, racine):
        self.racine = [racine]
    
    def get_racine(self):
        return self.racine[0]
    
    def set_gauche(self, gauche):
        self.gauche = gauche
    
    def get_gauche(self):
        return self.gauche
    
    def set_droite(self, droite):
        self.droite = droite
    
    def get_droite(self):
        return self.droite
    
    def estVide(self):
        return self.racine == [None]
    
    def taille(self):
        if self.estVide():
            return 0
        else:
            gauche_taille = self.get_gauche().taille() if self.get_gauche() is not None else 0
            droite_taille = self.get_droite().taille() if self.get_droite() is not None else 0
            return 1 + gauche_taille + droite_taille
   
    def prefixe(self):
        if self.estVide():
            return
        print(self.get_racine())
        if self.get_gauche() is not None:
            self.get_gauche().prefixe()
        if self.get_droite() is not None:
            self.get_droite().prefixe()
        

    def infixe(self):
        if self.estVide():
            return
        if self.get_gauche() is not None:
            self.get_gauche().infixe()
        print(self.get_racine())
        if self.get_droite() is not None:
            self.get_droite().infixe()
    
    def postfixe(self):
        if self.estVide():
            return
        if self.get_gauche() is not None:
            self.get_gauche().postfixe()
        if self.get_droite() is not None:
            self.get_droite().postfixe()
        print(self.get_racine())

    def hauteur(self):
        if self.estVide():
            return 0
        else:
            gauche_hauteur = self.get_gauche().hauteur() if self.get_gauche() is not None else 0
            droite_hauteur = self.get_droite().hauteur() if self.get_droite() is not None else 0
            return 1 + max(gauche_hauteur, droite_hauteur)
        
        
    def estABR(self, min=float('-inf'), max=float('inf')):
        if self.estVide():
            return True
        else:
            racine_val = self.get_racine()
            if racine_val < min or racine_val > max:
                return False
            else:
                gauche = self.get_gauche()
                droite = self.get_droite()
                if gauche is not None and not gauche.estABR(min, racine_val):
                    return False
                if droite is not None and not droite.estABR(racine_val, max):
                    return False
                return True


    def estEquilibre(self):
        if self.estVide():
            return True
        else:
            gauche_hauteur = self.get_gauche().hauteur() if self.get_gauche() is not None else -1 #Si on avait mis 0 à la place de -1, cela aurait compté le sous-arbre vide comme un niveau de hauteur, ce qui est incorrect.
            droite_hauteur = self.get_droite().hauteur() if self.get_droite() is not None else -1
            if abs(gauche_hauteur - droite_hauteur) <= 1:
                if self.get_gauche() is not None:
                    est_gauche_equilibre = self.get_gauche().estEquilibre()
                else:
                    est_gauche_equilibre = True
                if self.get_droite() is not None:
                    est_droite_equilibre = self.get_droite().estEquilibre()
                else:
                    est_droite_equilibre = True
                return est_gauche_equilibre and est_droite_equilibre
            else:
                return False