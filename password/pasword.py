import re

# Définir une expression régulière pour vérifier si le mot de passe respecte les exigences
regex = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$')

while True:
    # Demander à l'utilisateur de choisir un mot de passe
    password = input("Choisissez un mot de passe : ")

    # Vérifier si le mot de passe choisi respecte les exigences de sécurité
    if regex.match(password):
        print("Mot de passe valide.")
        break
    else:
        print("Le mot de passe doit contenir au moins 8 caractères, au moins une lettre majuscule, au moins une lettre minuscule, au moins un chiffre, et au moins un caractère spécial (!, @, #, $, %, ^, &, *). Veuillez choisir un nouveau mot de passe.")
import hashlib

password = input("Entrez votre mot de passe : ")

# Convertir le mot de passe en une chaîne d'octets
password_bytes = password.encode('utf-8')

# Calculer le hachage SHA-256 du mot de passe
hash_object = hashlib.sha256(password_bytes)
hash_hex = hash_object.hexdigest()

print("Le hachage SHA-256 de votre mot de passe est :", hash_hex)
