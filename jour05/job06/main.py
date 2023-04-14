def arrondir_notes(notes):
    arrondies = []
    for note in notes:
        if note < 40:
            arrondies.append(note)
        elif note % 5 > 2 and note >= 38:
            arrondies.append(note + 5 - (note % 5))
        else:
            arrondies.append(note)
    return arrondies
notes = [33, 47, 62, 78, 81, 85, 89, 92, 97]
arrondies = arrondir_notes(notes)
print(arrondies)
