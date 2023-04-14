numbers = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

rounded_numbers = [round(num) for num in numbers]  # arrondir les nombres
sorted_numbers = sorted(rounded_numbers)  # trier la liste dans l'ordre croissant

print(sorted_numbers)
