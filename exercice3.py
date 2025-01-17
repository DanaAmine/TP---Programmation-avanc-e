try:
    montant = float(input("Montant total : "))
except ValueError:
    print("La saisie doit être un nombre")
    exit()

try:
    nb_articles = int(input("Nombre d'articles : "))
except ValueError:
    print("La saisie doit être un entier")
    exit()

jours_semaine = ["Dimanche", "Samedi", "Lundi", "Mardi", "Mercredi", "Jeudi"]
jour_semaine = input("Jour de la semaine : ")
if jour_semaine not in jours_semaine:
    print("Vous devez saisir un jour de la semaine complet et valide")
    exit()

remise = 0.10 if jour_semaine not in ["Samedi", "Dimanche"] else 0.20
remise += 0.5 if nb_articles > 5 else 0

print(f"Prix total après remise : {round(montant * (1 - remise), 2)} dinars")
