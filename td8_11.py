import math
import random


# Volume d'un cone droit suite à la saisie d'un rayon et d'une hauteur
def volume_cone(rayon, hauteur):
    volume = math.pi * rayon ** 2 * hauteur / 3
    return volume


# diviseurs, nombre de diviseurs, ou "premier" d'un nombre entier positif
def diviseurs(nombre):
    liste_diviseurs = []
    try:
        if int(nombre) > 0:
            for i in range(1, nombre):
                if nombre % i == 0:
                    liste_diviseurs.append(i)
            if len(liste_diviseurs) > 0:
                phrase = "Les diviseurs de {0} sont : {1}, il y en a {2} au total".format(nombre, liste_diviseurs,
                                                                                          len(liste_diviseurs))
            else:
                phrase = "{0} est un nombre premier".format(nombre)
        else:
            phrase = "Ceci n'est pas un nombre positif"
        return phrase
    except:
        print("Erreur, merci d'entrer un nombre positif")


# approximer e, n>50
def get_e(n_max):
    valeur_attendue = 2.71828182845904523536
    try:
        e = 0
        for n in range(n_max):
            factorielle = math.factorial(n)
            inv_fact = 1 / factorielle
            e += inv_fact
        diff = abs(valeur_attendue - e)
        return e, diff
    except:
        print("Erreur factoriel")


# sequencage adn
def adn_valide(sequence):
    if len(sequence) > 0:
        for lettre in range(len(sequence)):
            if lettre != "a" or lettre != "t" or lettre != "c" or lettre != "g":
                return False
        return True
    else:
        return False


def saisie_adn(longueur):
    liste_valeurs_possibles = ["a", "t", "c", "g"]
    chaine = ""
    for lettre in range(longueur):
        aleatoire = random.randint(0, 3)
        chaine += liste_valeurs_possibles[aleatoire]
    return chaine


def proportion_adn(chaine, sequence):
    occurences = chaine.count(sequence)
    proportion = occurences * 100 / (len(chaine) / len(sequence))
    return occurences, proportion


# renvoyer le minimum, le maximum et la moyenne d'une liste
def minMaxMoy(liste):
    try:
        min_list = min(liste)
        max_list = max(liste)
        moy = sum(liste) / len(liste)
        return min_list, max_list, moy
    except:
        print("erreur dans la liste")


# transformer en chiffres romains :
def romaniser(nombre):
    chaine_romaine = ""
    m = d = c = l = x = v = 0
    if nombre > 1000:
        m = nombre // 1000
        nombre = nombre % 1000
    if nombre > 500:
        d = nombre // 500
        nombre = nombre % 500
    if nombre > 100:
        c = nombre // 100
        nombre = nombre % 100
    if nombre > 50:
        l = nombre // 50
        nombre = nombre % 50
    if nombre > 10:
        x = nombre // 50
        nombre = nombre % 50
    if nombre > 5:
        v = nombre // 10
        nombre = nombre % 5
