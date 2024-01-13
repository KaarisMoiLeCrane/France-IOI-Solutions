dice1 = int(input())
dice2 = int(input())

somme = dice1 + dice2

if somme >= 10:
    print("Taxe spéciale !")
    print(36)
else:
    print("Taxe régulière")
    print(somme * 2)
