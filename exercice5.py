print("Coureur 1 :")
nom_coureur_un = input("Nom : ")
try:
    temps_coureur_un = float(input("Temps (en secondes) : "))
except ValueError:
    print("Le temps doit être un nombre décimal ou entier")
    exit()

print("Coureur 2 :")
nom_coureur_deux = input("Nom : ")
try:
    temps_coureur_deux = float(input("Temps (en secondes) : "))
except ValueError:
    print("Le temps doit être un nombre décimal ou entier")
    exit()

if temps_coureur_un > temps_coureur_deux:
    print(f"Le coureur le plus rapide est : {nom_coureur_deux}")
elif temps_coureur_un < temps_coureur_deux:
    print(f"Le coureur le plus rapide est : {nom_coureur_un}")
else:
    print(f"{nom_coureur_un} et {nom_coureur_deux} ont le même temps")
