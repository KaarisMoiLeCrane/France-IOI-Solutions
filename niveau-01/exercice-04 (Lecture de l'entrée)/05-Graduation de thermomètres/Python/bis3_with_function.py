def affiche(debut: int, fin: int):
    """Affiche les nombres de [début] à [fin] inclus.

    Args:
        debut (int): Le début de la boucle (nombre inclus)
        fin (int): La fin de la boucle (nombre inclus)
    """

    assert (
        debut <= fin
    ), "Cela ne devrait jamais arriver, mais cela arrive de temps en temps. \nEnvoyez un mail à [mail] si vous rencontrez ce problème."

    print(debut)
    if debut != fin:
        affiche(debut + 1, fin)


temp_min = int(input())
temp_max = int(input())
affiche(temp_min, temp_max)
