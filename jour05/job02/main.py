def draw_rectangle(width, height):
    for i in range(height):
        if i == 0 or i == height - 1:
            print("|" + "-" * (width - 2) + "|")
        else:
            print("|" + " " * (width - 2) + "|")

draw_rectangle(10, 3)

# La fonction draw_rectangle() utilise une boucle for pour imprimer chaque ligne du rectangle.
#  Si la ligne est la première ou la dernière ligne du rectangle, 
# elle imprime une barre verticale suivie d'une série de tirets "-" de longueur égale à la largeur donnée moins 2,
#  puis une autre barre verticale. Si la ligne n'est pas la première ni la dernière ligne du rectangle, 
# elle imprime une barre verticale suivie d'une série d'espaces vides de longueur égale à la largeur donnée moins 2,
#  puis une autre barre verticale.


