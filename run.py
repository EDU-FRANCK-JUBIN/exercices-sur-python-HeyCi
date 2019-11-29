import td8_11

print(td8_11.volume_cone(5, 8))
print(td8_11.diviseurs(12))
print(td8_11.get_e(80))

chaine = td8_11.saisie_adn(50)
sequence = td8_11.saisie_adn(2)
print(chaine)
print(sequence)
occurence, proportion = td8_11.proportion_adn(chaine, sequence)
print("occurences : {0}, ce qui fait {1} %".format(occurence, proportion))

liste = [10, 18, 14, 20, 12, 16]
min_list, max_list, moy = td8_11.minMaxMoy(liste)
print("minimum: {0}, maximmum: {1}, moyenne: {2}".format(min_list, max_list, moy))
