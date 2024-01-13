for _ in range(int(input())):
    x = int(input())
    y = int(input())
    print(
        [
            "En dehors de la feuille",
            "Dans une zone rouge",
            "Dans une zone bleue",
            "Dans une zone jaune",
        ][
            0
            if not (0 < x < 90 and 0 < y < 70)
            else 1
            if ((15 < x < 45) or (60 < x < 85)) and y > 60
            else 2
            if not (25 < x < 50 and 20 < y < 45) and 10 < x < 85 and 10 < y < 55
            else 3
        ]
    )
