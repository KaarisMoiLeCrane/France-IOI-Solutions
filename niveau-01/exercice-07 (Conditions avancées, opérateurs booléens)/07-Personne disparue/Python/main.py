numero_personne_cherchee = int(input())
nbr_personnes = int(input())
est_sorti = False

for _ in range(nbr_personnes):
    numero = int(input())
    if numero == numero_personne_cherchee:
        est_sorti = True

if est_sorti:
    print("Sorti de la ville")
else:
    print("Encore dans la ville")
