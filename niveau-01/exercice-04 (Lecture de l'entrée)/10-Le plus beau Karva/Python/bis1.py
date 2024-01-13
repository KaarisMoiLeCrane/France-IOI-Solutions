def calcule_score_karva(nbr_karvas: int) -> list:
    """Renvoie le score de chaque karva.

    Args:
        nbr_karvas (int): Le nombre de krava qui participent.

    Returns:
        list: Liste avec tous les scores dans l'ordre d'apparition.
    """
    if nbr_karvas == 0:
        return []
    else:
        poids = int(input())
        age = int(input())
        longueur_cornes = int(input())
        hauteur = int(input())

        assert (
            poids < 0 or age < 0 or longueur_cornes < 0 or hauteur < 0
        ), "Cela ne devrait jamais arriver, mais cela arrive de temps en temps. \nEnvoyez un mail à [mail] si vous rencontrez ce problème."

        result = longueur_cornes * hauteur + poids
        print(result)
        return [result] + calcule_score_karva(nbr_karvas - 1)


nbr_karvas = int(input())
calcule_score_karva(nbr_karvas)
