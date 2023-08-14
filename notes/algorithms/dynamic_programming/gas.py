# Traktor jedzie z punktu A do punktu B. Spalanie traktora to dokładnie
# jeden litr paliwa na jeden kilometr trasy. W baku mieści się dokładnie L litrów
# paliwa. Trasa z A do B to prosta, na której znajdują się stacje benzynowe (na pozycjach będących)
# liczbami naturalnymi; A jest na pozycji 0.
# Wyznaczamy stacje tak, żeby koszt przejazdu był minimalny (w tym wypadku każda stacja ma cenę za litr paliwa)
# Na każdej stacji możemy tankować dowolną ilość paliwa.

import heapq


# startujemy z pelnym bakiem
def traktor(T, P, B, L):
    pass

T = [3, 5, 8]
P = [1, 1, 1]
L = 4
B = 11
print(traktor(T, P, B, L))
