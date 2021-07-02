# Sprawdź, które spośród danych liczb są liczbami pierwszymi
# Input
# n - liczba testów n<100000, w kolejnych liniach n liczb z przedziału [1..10000]
# Output
# Dla każdej liczby słowo TAK, jeśli liczba ta jest pierwsza, słowo: NIE, w przeciwnym wypadku.


def is_prime(number):
    if number < 2:
        return "NIE"
    x = 2
    while x**2 <= number:
        if number % x == 0:
            return "NIE"
        x += 1
    return "TAK"


n = int(input())
for i in range(n):
    num = int(input())
    print(is_prime(num))
