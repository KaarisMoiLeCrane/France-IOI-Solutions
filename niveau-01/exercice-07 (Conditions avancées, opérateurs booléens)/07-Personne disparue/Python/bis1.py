numero_personne = int(input())
nbr_personnes = int(input())
numeros_personnes = iter(int(input()) for _ in range(nbr_personnes))

est_sorti = any(numero_personne == num for num in numeros_personnes)
print("Sorti de la ville" if est_sorti else "Encore dans la ville")