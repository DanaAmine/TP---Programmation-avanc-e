try:
    temperature = int(input("Veuillez saisir la température : "))
    if temperature < 0:
        print("Il gèle !")
    elif temperature < 10:
        print("Il fait froid !")
    elif temperature < 20:
        print("Il fait frais")
    print("Restez prudent !")
except ValueError:
    print("La température doit être un entier valide")
