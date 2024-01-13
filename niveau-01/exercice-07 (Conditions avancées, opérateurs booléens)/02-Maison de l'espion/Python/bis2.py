position_actuelle = int(input())
nbr_villages = int(input())
positions_villages = iter(int(input()) for _ in range(nbr_villages))

print(
    sum(
        1
        for position_village in positions_villages
        if abs(position_actuelle - position_village) <= 50
    )
)
