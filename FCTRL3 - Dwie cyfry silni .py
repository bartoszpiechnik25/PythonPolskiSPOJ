# Niech n będzie nieujemną liczbą całkowitą. Liczbę n! (czytaj n-silnia) definiuje się następująco. Jeśli n ≤ 1, to
# n! = 1. Dla n > 1, n! jest równe iloczynowi wszystkich liczb od 1 do n, czyli n! = 1 * 2 * ... * n. Na przykład
# 4! = 1*2*3*4 = 24.
# Napisz program, który:
# wczyta ze standardowego wejścia nieujemną liczbę całkowitą n,
# policzy cyfrę dziesiatek oraz cyfrę jedności w zapisie dziesiętnym liczby n!,
# wypisze wynik na standardowe wyjście.
# Wejście
# W pierwszej linii wejścia znajduje się jedna liczba całkowia D (1≤D≤30), oznaczjąca liczbę przypadków do rozważenia.
# Opis każdego przypadku składa się z jednej linii, w której znajduje się jedna nieujemna liczba całkowita
# n (0 ≤ n ≤ 1 000 000 000).
# Wyjście
# Dla każdego przypadku z wejścia. Twój program powinien wypisać w osobnej linii dokładnie dwie cyfry
# (oddzielone pojedynczą spacją): cyfrę dziesiątek i cyfrę jedności liczby n! zapisanej w systemie dziesiętnym.


def dwie_cyfry(a):
    var = 1
    if a < 10:
        for i in range(1, a + 1):
            var *= i
        if a < 4:
            return [0] + [var]
        else:
            return [(var // 10) % 10] + [var % 10]
    else:
        return [0] + [0]


t = int(input())

for _ in range(t):
    x = int(input())
    print(*dwie_cyfry(x))


