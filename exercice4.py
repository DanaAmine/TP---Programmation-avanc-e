try: 
    age_un = int(input("Veuillez saisir l'âge de la première personne : "))
    age_deux = int(input("Veuillez saisir l'âge de la deuxième personne : "))
except ValueError:
    print("La saisie doit être un entier")
    exit()

if age_un > age_deux:
    print(f"L'âge le plus élevé est : {age_un}")
elif age_un < age_deux:
    print(f"L'âge le plus élevé est : {age_deux}")
else:
    print("Les deux personnes ont le même âge !")
