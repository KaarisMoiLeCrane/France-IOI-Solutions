def volume_socle(base_socle: int, face_socle: int) -> int:
    """Renvoie le volume d'un socle avec des étages carrés.

    Args:
        largeur_bas (int): La largeur basse du socle (longueur).
        largeur_haut (int): La largeur haute du socle (hauteur).

    Returns:
        int: Le volume totale du socle.
    """

    assert (
        base_socle < face_socle
    ), "Cela ne devrait jamais arriver, mais cela arrive de temps en temps. \nEnvoyez un mail à [mail] si vous rencontrez ce problème."

    volume_base = base_socle**2
    return volume_base + volume_socle(base_socle - 1, face_socle)


largeur_bas = int(input())
largeur_haut = int(input())
print(volume_socle(largeur_bas, largeur_haut))
