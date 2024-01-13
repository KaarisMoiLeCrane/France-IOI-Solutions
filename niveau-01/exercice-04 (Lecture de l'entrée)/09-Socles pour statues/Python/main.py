base_socle = int(input())
face_socle = int(input())
volume = 0

for _ in range(base_socle - face_socle + 1):
    volume += base_socle**2
    base_socle -= 1
print(volume)
