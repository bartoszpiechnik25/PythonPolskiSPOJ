# Dla danych dwóch liczb naturalnych a i b, wyznaczyć ostatnią cyfrę liczby ab.
#
# Zadanie
# Napisz program, który:
# wczyta ze standardowego wejścia: podstawę a oraz wykładnik b,
# wyznaczy ostatnią cyfrę liczby ab,
# wypisze wynik na standardowe wyjście.
# Wejście
# W pierwszej linii wejścia znajduje się jedna liczba całkowia D (1≤D≤10), oznaczjąca liczbę przypadków do rozważenia.
# Opis każdego przypadku podany jest w jednym wierszu, zawierającym dwie liczby naturalne a i b oddzielone pojedynczym
# odstępem (spacją), takie, że (1 ≤ a,b ≤ 1 000 000 000).
#
# Wyjście
# Dla każdego przypadku z wejścia Twój program powinien wypisać (w osobnej linii dla każdego przypadku z wejścia) cyfrę
# jedności liczby ab zapisanej dziesiętnie.


def power(a, b):
    if b % 4 == 1:
        return a % 10
    elif b % 4 == 2:
        return a * a % 10
    elif b % 4 == 3:
        return (a**3) % 10
    elif b % 4 == 0:
        return (a**4) % 10


t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    print(power(x, y))


