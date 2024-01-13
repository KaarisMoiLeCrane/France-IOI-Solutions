nbr_paires = int(input())
for _ in range(nbr_paires):
    x_min1 = int(input())
    x_max1 = int(input())
    y_min1 = int(input())
    y_max1 = int(input())

    x_min2 = int(input())
    x_max2 = int(input())
    y_min2 = int(input())
    y_max2 = int(input())

    if ((x_max2 <= x_min1) or (x_max1 <= x_min2)) or (
        (y_max2 <= y_min1) or (y_max1 <= y_min2)
    ):
        print("NON")
    else:
        print("OUI")
