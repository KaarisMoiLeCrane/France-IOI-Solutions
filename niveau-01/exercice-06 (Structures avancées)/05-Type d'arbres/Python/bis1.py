hauteur = int(input())
folioles = int(input())

print(
    "Falarion"
    if hauteur <= 8 and folioles <= 5
    else (
        "Tinuviel"
        if hauteur <= 5 and folioles >= 8
        else (
            "Calaelen"
            if hauteur >= 10 and folioles >= 10
            else ("Dorthonion" if hauteur >= 12 and folioles <= 7 else "")
        )
    )
)
