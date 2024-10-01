# primes.py

def isprime(p):
    """
    Détermine si un nombre est premier.

    Args:
        p: Un entier à tester.

    Returns:
        True si p est un nombre premier, False sinon.

    Un nombre est considéré comme premier s'il est supérieur à 1 et
    n'a pas d'autres diviseurs que 1 et lui-même.
    """
    if p <= 1:
        return False
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            return False
    return True

    pass
