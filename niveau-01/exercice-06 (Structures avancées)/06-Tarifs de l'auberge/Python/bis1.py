age = int(input())
poids = int(input())

if age < 10:
    print(5)
elif age != 60:
    prix = 30 + 10 if poids >= 20 else 30
    print(prix)
else:
    print(0)
