try:
    nombre = int(input("Nombre : "))
except ValueError: 
    print("Vous devez entrer un entier")
    exit()

resultat = ""
if nombre % 3 == 0:
    resultat += "Fizz"
if nombre % 5 == 0:
    resultat += "Buzz"

print("Résultat :")
print(resultat)
