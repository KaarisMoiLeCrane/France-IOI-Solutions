nbr_maisons = int(input())
x_max, x_min, y_max, y_min = 0, 1000 * 1000, 0, 1000 * 1000

for _ in range(nbr_maisons):
    x, y = int(input()), int(input())

    x_max = max(x_max, x)
    x_min = min(x_min, x)
    y_max = max(y_max, y)
    y_min = min(y_min, y)

print(((y_max - y_min) + (x_max - x_min)) * 2)
