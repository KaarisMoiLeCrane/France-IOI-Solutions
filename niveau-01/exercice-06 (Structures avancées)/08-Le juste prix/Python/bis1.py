print(
    min(
        (
            (
                lambda marchands: (
                    min_price := min(marchands),
                    marchands.index(min_price) + 1,
                )
            )(list(map(int, (input() for _ in range(int(input()))))))
        )[1],
        default=1,
    )
)
