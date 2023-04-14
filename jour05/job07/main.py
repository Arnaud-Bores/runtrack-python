mot = input("Entrez un mot sans espace ni caractère spécial : ")

# Vérification que le mot contient seulement des lettres
if not mot.isalpha():
    print("Le mot doit contenir seulement des lettres de l'alphabet sans accent ni majuscule.")
    exit()

# Conversion du mot en une liste de caractères pour pouvoir le manipuler plus facilement
mot_list = list(mot)

# Recherche des deux caractères à échanger
for i in range(len(mot_list) - 1, 0, -1):
    if mot_list[i - 1] < mot_list[i]:
        j = i
        while j < len(mot_list) and mot_list[j] > mot_list[i - 1]:
            j += 1
        break

# Échange des deux caractères
mot_list[i - 1], mot_list[j - 1] = mot_list[j - 1], mot_list[i - 1]

# Tri des caractères suivants dans l'ordre croissant
mot_list[i:] = sorted(mot_list[i:])

# Reconstruction du mot
nouveau_mot = "".join(mot_list)

print("Le nouveau mot est :", nouveau_mot)
