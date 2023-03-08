seuil_P=2.3
seuil_V=10
press=float(input("Entre la pression actuelle: "))
volume=float(input("Entre la volume actuelle: "))

if press > seuil_P and volume > seuil_V:
    print('Arret')
elif press >seuil_P: 
    print('Add Volume')
elif volume >seuil_V: 
    print('diminue volume')
else:
    print("All good")