print("Entrez le nom des villes une par une [tapez 'stop' pour quitter]")
nom_ville = input()
villes = {}
MILLION = 10 ** 6

while nom_ville.lower() != "stop":
    villes[nom_ville] = len(nom_ville) * MILLION
    nom_ville = input()

villes = dict(sorted(villes.items(), key=lambda x: x[1], reverse=True))

for ville, population in villes.items():
    print(f"Ville : {ville} , Population : {population}")
