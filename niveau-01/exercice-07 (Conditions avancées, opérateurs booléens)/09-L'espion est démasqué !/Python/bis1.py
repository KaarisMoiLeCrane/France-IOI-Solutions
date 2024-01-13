for _ in range(int(input())):
    print(
        [
            "Impossible",
            "Peu probable",
            "Peu probable",
            "Probable",
            "Probable",
            "Très probable",
        ][
            int(178 <= int(input()) <= 182)
            + int(int(input()) >= 34)
            + int(int(input()) < 70)
            + int(int(input()) == 0)
            + int(int(input()) == 1)
        ]
    )
