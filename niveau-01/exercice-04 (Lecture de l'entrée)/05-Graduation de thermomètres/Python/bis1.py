temp_min = int(input())
temp_max = int(input())
temperature_actuel = temp_min

for _ in range(temp_max - temp_min + 1):
    print(temperature_actuel)
    temperature_actuel = temperature_actuel + 1
