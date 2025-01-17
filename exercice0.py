try:
    nb_personnes = int(input("Combien de personnes ont besoin d'un transport ? "))
    nb_places_taxi = int(input("Combien de personnes peuvent entrer dans un taxi ? "))
except ValueError:
    print("La saisie doit être un nombre entier")
    exit()

print(f"Le nombre de taxis nécessaires est {nb_personnes // nb_places_taxi if nb_personnes % nb_places_taxi == 0 else nb_personnes // nb_places_taxi + 1}")
