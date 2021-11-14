#  Napisz program, który dla danego wzorca P (ang. pattern) i tekstu T wypisze pozycje, na których znajduje się wzorzec
#  P jako podsłowo tekstu T.
# Wejście
# W pierwszym wierszu danych znajduje się liczba natralna T (0 < T < 11) oznaczająca liczbę zestawów danych.
# Każdy zestaw danych podany jest w trzech wierszach. Pierwszy zawiera jedną liczbę naturalną n - oznaczającą długość
# wzorca P ( n <= 1000000 ). Drugi wiersz zawiera wzorzec P - napis złożony z n liter angielskiego alfabetu (a-z, A-Z).
# Trzeci wiersz zawiera test T czyli ciąg liter alfabetu angielskiego zakończony znakiem nowego wiersza.
# Wyjście
# Dla każdego zestawu danych wypisz pozycje na których wzorzec P pasuje w tekscie T. Zakładamy, że litery tekstu T
# numerowane są od zera.
import re


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        pattern = input()
        text = input()
        for number in re.finditer(pattern[0], text):
            oc = number.start()
            if pattern == text[oc:oc+n]:
                print(oc)
