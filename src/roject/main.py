import random

# Génère un nombre aléatoire entre 1 et 10
nombre_a_deviner = random.randint(1, 10)

# Demande à l'utilisateur de deviner le nombre
print("Devinez le nombre entre 1 et 10 !")
essai = int(input("Entrez votre nombre : "))

# Vérifie si l'utilisateur a deviné correctement
if essai == nombre_a_deviner:
    print("Bravo ! Vous avez deviné le bon nombre.")
else:
    print(f"Dommage ! Le nombre était {nombre_a_deviner}.")
