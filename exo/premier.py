def estPremier(n) :
    """
    Retourne True si n est premier, False sinon. n doit être un entier.

    Les nombres négatifs ne sont pas premiers :
    >>> estPremier(-1)
    False

    Les nombres 0 et 1 ne sont pas premiers :
    >>> estPremier(0)
    False

    >>> estPremier(1)
    False

    Un nombre premier n'est divisible que par 1 et par lui-même :
    >>> estPremier(2)
    True

    >>> estPremier(4)
    False

    >>> estPremier(11)
    True
    """
    if n <= 1 :
        return False
    for i in range(2, n) :
        if (n % i == 0) :
            return False
    return True