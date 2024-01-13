def intersecte(min1: int, max1: int, min2: int, max2: int) -> bool:
    """Vérifie si un groupement de valeurs d'une paire s'intersectent.

    Args:
        min1 (int): La valeur minimale du premier élément.
        max1 (int): La valeur maximale du premier élément.
        min2 (int): La valeur minimale du deuxième élément.
        max2 (int): La valeur maximale du deuxième élément.

    Returns:
        bool: \"true\" s'ils s'intersectent sinon \"false\".
    """
    return (max2 > min1) and (max1 > min2)


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

    if intersecte(x_min1, x_max1, x_min2, x_max2) and intersecte(
        y_min1, y_max1, y_min2, y_max2
    ):
        print("OUI")
    else:
        print("NON")
