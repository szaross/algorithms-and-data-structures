# Szymon Szarek
# Zlozonosc czasowa - O(n^2)
# Przechodzę przez wszystkie elementy tablicy i rozpatruję przypadek, 
# w którym ten element jest środkiem palindromu. Połowę długości aktualnego 
# kandydata na najdłuższy palindrom zapisuję w zmiennej delta; nie rozpatruję
# elementu jako środka, jeżeli na pozycjach [i +/- delta] są różne znaki. 
# Palindrom weryfikuję iterując od środka, aż dojdę do momentu, w którym 
# nie można już bardziej go poszerzyć.


from zad1testy import runtests

def ceasar( s ):
    l=len(s)
    max_length=1
    delta=1
    for i in range(1,l):
        if i+delta>=l:
            return max_length
        if s[i+delta]==s[i-delta]:
            a=1
            n=1
            while i>=a and l>i+a and s[i+a]==s[i-a]:
                n+=2
                a+=1
            else:
                if n>max_length:
                    max_length=n
                    delta=max_length//2

    return max_length
# def ceasar( s ):
#     maxi = 1
#     for i in range(len(s)):

#         l = i - 1
#         p = i + 1

#         while True:
#             if l < 0 or p > len(s) - 1:
#                 break
#             if s[l] == s[p]:
#                 if p - l + 1 > maxi:
#                     maxi = p - l + 1
#                 l -= 1
#                 p += 1
#             else:
#                 break
#     return maxi


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )
