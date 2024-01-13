total_mesures = int(input())
temperature_min = int(input())
temperature_max = int(input())
nbr_mesures = 1
temperature = int(input())

while (
    nbr_mesures <= total_mesures and temperature_min <= temperature <= temperature_max
):
    print("Rien à signaler")
    if nbr_mesures != total_mesures:
        temperature = int(input())
    nbr_mesures += 1

if temperature < temperature_min or temperature > temperature_max:
    print("Alerte !!")
