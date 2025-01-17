nom = input("Veuillez entrer votre nom : ")
if nom == "VIP":
    print("Profitez du spectacle gratuitement !")
else:
    PRIX_BILLET = 15.50
    try:
        nb_billets = int(input("Combien de billets souhaitez-vous acheter ? "))
    except ValueError:
        print("Le nombre de billets doit être un entier")
        exit()
    if nb_billets == 0:
        print("Vous ne pouvez pas assister au spectacle sans acheter au moins un billet !")
    else:
        print(f"Le coût total est de {PRIX_BILLET * nb_billets}")
