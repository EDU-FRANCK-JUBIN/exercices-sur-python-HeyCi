pi = 3.14159265359
pi_wallis = 2
for i in range(1, 100000):
    pi_wallis *= 4 * (i ** 2) / (4 * (i ** 2) - 1)
print("résultat formule de wallis : {0}".format(pi_wallis))
print("valeur usuelle de pi : {0}".format(pi))
print("écart : {0}".format(pi_wallis - pi))

liste_depart = [32, 5, 12, 8, 3, 75, 2, 15]
liste_pairs = []
liste_impairs = []
for element in liste_depart:
    if element % 2 == 0:
        liste_pairs.append(element)
    else:
        liste_impairs.append(element)
print("\nliste de départ : {0}\nnombres pairs : {1}\nnombres impairs : {2}".format(liste_depart, liste_pairs,
                                                                                   liste_impairs))


def max(a, b):
    if a > b:
        return a
    else:
        return b


def max_3(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


def factorielle(a):
    fact = 1
    for i in range(1, a+1):
        fact *= i
    return fact


print(factorielle(5))

