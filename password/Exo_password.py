
import random
mdp_valide = False

while not mdp_valide:
    mdp = input("Veuillez entrer votre mot de passe :\n")
    if len(mdp) < 8:
        print("Votre mot de passe doit contenir au moins 8 caractères.")
        continue
    up = False
    low = False
    num = False
    spe = False
    for char in mdp:
        if char.isupper():
            up = True
        if char.islower():
            low = True
        if char.isdigit():
            num = True
        if char in ["!", "@", "#", "$", "%", "^", "&", "*"]:
            spe = True
    if not up:
        print("Votre mot de passe doit contenir au moins 1 lettre majuscule.")
        continue
    if not low:
        print("Votre mot de passe doit contenir au moins 1 lettre minuscule.")
        continue
    if not num:
        print("Votre mot de passe doit contenir au moins 1 chiffre.")
        continue
    if not spe:
        print("Votre mot de passe doit contenir au moins 1 caractère spécial. (!, @, #, $, %, ^, &, *)")
        continue
    else:
        print("Votre mot de passe est valide ! Bienvenue !")
        mdp_valide = True

import hashlib

password = "monMotDePasse123"

hash_object = hashlib.sha256()
hash_object.update(password.encode())

hashed_password = hash_object.hexdigest()

print("Mot de passe d'origine : ", password)
print("Mot de passe crypté : ", hashed_password)
