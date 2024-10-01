'''
Ceci est le fichier principal main.py
'''

from primes import isprime

#### Fonction principale
def main():
    """
    Fonction principale qui affiche les nombres premiers de 0 à 99.
    """
    isprime(8)

    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()

if __name__ == "__main__":
    help(main)
    main()
