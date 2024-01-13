nbr_secret = int(input())
nb_proposition = int(input())
nbr_essais = 1

while nb_proposition != nbr_secret:
    print("c'est plus") if nb_proposition < nbr_secret else print("c'est moins")
    nbr_essais += 1
    nb_proposition = int(input())

print("Nombre d'essais nécessaires :")
print(nbr_essais)
