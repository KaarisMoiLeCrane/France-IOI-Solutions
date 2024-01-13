print(
    5
    if (age := int(input())) < 10
    else (
        30 + 10
        if age != 60 and (poids := int(input())) >= 20
        else (30 if age != 60 else 0)
    )
)
