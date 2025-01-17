try:
    annee = int(input("Veuillez saisir une année : "))
except ValueError: 
    print("Vous devez saisir une année valide")
    exit()

bissextile = False
if annee % 4 == 0: 
    if annee % 100 == 0:
        bissextile = annee % 400 == 0
    else:
        bissextile = True

if bissextile: 
    print("C'est une année bissextile")
else:
    print("Ce n'est pas une année bissextile")
