def ajouter_mangue(fruits):
    fruits.insert(2, "Mangue")
    return fruits
fruits = ["pomme", "cerise", "orange", "Melon"]
nouveaux_fruits = ajouter_mangue(fruits)
print(nouveaux_fruits)
