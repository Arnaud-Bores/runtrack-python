def afficher_produits(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print("artichaut, aubergine, navet")
    else:
        print("Aucun produit disponible pour cette combinaison de type et de saison.")

# Exemples d'utilisation
afficher_produits("fruits", "hiver")  # Affiche "orange, mandarine et kiwi"
afficher_produits("fruits", "ete")  # Affiche "Poire, fraise, cassis"
afficher_produits("legume", "hiver")  # Affiche "carotte, topinambour, endive"
afficher_produits("legume", "ete")  # Affiche "artichaut, aubergine, navet"
afficher_produits("viande", "ete")  # Affiche "Aucun produit disponible pour cette combinaison de type et de saison."
