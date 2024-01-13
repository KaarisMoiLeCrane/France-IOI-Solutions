x_min = int(input())
x_max = int(input())
y_min = int(input())
y_max = int(input())
nbr_maisons = int(input())
nbr_a_fouiller = 0

for _ in range(nbr_maisons):
    x = int(input())
    y = int(input())
    if (x_min <= x) and (x <= x_max) and (y_min <= y) and (y <= y_max):
        nbr_a_fouiller += 1
print(nbr_a_fouiller)
