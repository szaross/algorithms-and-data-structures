# Szymon Szarek
# Zlozonosc obliczeniowa: O(V^3logV)
# Algorytm opiera sie na algorytmie dijkstry. W kazdym instancji pamietamy czy juz zrabowalismy zamek czy jeszcze nie.
# Jezeli tak, to do kolejki dodajemy przekalkulowane koszty przejscia, jezeli nie to rozwazamy dwie mozliwosci: albo rabujemy aktualny zamek
# albo idziemy dalej. Rozwiazanie trzymamy w zmiennej distance, jednak zwracamy je jezeli wiemy, ze zrabowalismy juz wszystkie zamki (w ten sposób wiemy, że aktualny koszt jest najmniejszy)


from egz1Atesty import runtests
import heapq


def gold(G, V, s, t, r):
    n = len(G)

    heap = [(0, s, False)]
    distance = float("inf")
    already_robbed = [False for _ in range(n)]
    while heap:
        balance, current, robbed = heapq.heappop(heap)
        # print(f"current:{current} bilans:{balance} robbed:{robbed}")
        if current == t:
            distance = min(distance, balance)
            if min(already_robbed) == True:
                return distance

        for neighbour, price in G[current]:
            if robbed == True:
                heapq.heappush(
                    heap,
                    (balance + 2 * price + r, neighbour, robbed),
                )
            else:
                heapq.heappush(
                    heap,
                    (balance + price, neighbour, robbed),
                )
                heapq.heappush(
                    heap,
                    (balance + 2 * price + r - V[current], neighbour, True),
                )
                already_robbed[current] = True

    return distance


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(gold, all_tests=True)
