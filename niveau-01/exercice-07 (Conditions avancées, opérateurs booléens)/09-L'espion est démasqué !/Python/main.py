conclusion = [
    "Impossible",
    "Peu probable",
    "Peu probable",
    "Probable",
    "Probable",
    "Très probable",
]

nbr_personnes = int(input())
for _ in range(nbr_personnes):
    taille = int(input())
    age = int(input())
    poids = int(input())
    avec_cheval = int(input())
    est_brun = int(input())

    nbr_criteres = int(178 <= taille <= 182)
    nbr_criteres += int(age >= 34)
    nbr_criteres += int(poids < 70)
    nbr_criteres += int(avec_cheval == 0)
    nbr_criteres += int(est_brun == 1)

    print(conclusion[nbr_criteres])
