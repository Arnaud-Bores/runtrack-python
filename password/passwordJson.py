import hashlib
import json

# Fonction pour hacher le mot de passe
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Fonction pour enregistrer les mots de passe hachés dans un fichier JSON
def save_passwords(passwords):
    with open('passwords.json', 'w') as f:
        json.dump(passwords, f)

# Fonction pour charger les mots de passe hachés depuis un fichier JSON
def load_passwords():
    try:
        with open('passwords.json', 'r') as f:
            passwords = json.load(f)
    except FileNotFoundError:
        passwords = {}
    return passwords

# Fonction pour ajouter un nouveau mot de passe
def add_password():
    website = input("Nom du site web : ")
    username = input("Nom d'utilisateur : ")
    password = input("Mot de passe : ")
    hashed_password = hash_password(password)
    passwords = load_passwords()
    passwords[website] = {'username': username, 'password': hashed_password}
    save_passwords(passwords)
    print("Mot de passe enregistré avec succès !")

# Fonction pour afficher tous les mots de passe enregistrés
def show_passwords():
    passwords = load_passwords()
    if not passwords:
        print("Aucun mot de passe enregistré.")
    else:
        for website, info in passwords.items():
            print(f"{website} : {info['username']} - {info['password']}")

# Menu principal
def main():
    while True:
        print("\nQue souhaitez-vous faire ?")
        print("1. Ajouter un nouveau mot de passe")
        print("2. Afficher tous les mots de passe enregistrés")
        print("3. Quitter")
        choice = input("Votre choix : ")
        if choice == '1':
            add_password()
        elif choice == '2':
            show_passwords()
        elif choice == '3':
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == '__main__':
    main()
