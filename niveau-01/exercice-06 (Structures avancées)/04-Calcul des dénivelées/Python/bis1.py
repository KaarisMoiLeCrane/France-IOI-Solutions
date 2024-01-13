sum(
    (total_montee := int(input()))
    if total_montee > 0
    else (total_descente := total_montee)
    for _ in range(int(input()))
)
print(
    total_montee,
    "\n",
    -total_descente,
)
