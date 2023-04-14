def distance_toilettes(marches, hauteur):
    distance_quotidienne = marches * hauteur * 5 / 100  # en mètres
    distance_hebdomadaire = distance_quotidienne * 7
    return f"Pour {marches} marches de {hauteur} cm, le gardien parcours {distance_hebdomadaire:.2f} m par semaine."

print(distance_toilettes(50, 20))
