base_socle = int(input())
face_socle = int(input())

volume = 0
largeur_socle = base_socle

while base_socle <= face_socle:
    volume += largeur_socle**2
    largeur_socle -= 1

print(volume)
