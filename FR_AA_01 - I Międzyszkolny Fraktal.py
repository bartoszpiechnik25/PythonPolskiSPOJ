# Rozpoczęła się I międzyszkolna edycja Fraktala. W zawodach biorą udział uczniowie z Olsztyna, Torunia, Elbląga oraz
# Działdowa.
# Z powodu pandemii koronawirusa i obowiązujących obostrzeń część z nich startuje zdalnie. Pozostałym zawodnikom
# Organizatorzy chcą zapewnić jak najwyższy poziom bezpieczeństwa. Aby to zrobić, muszą znać dokładną liczbę uczniów
# biorących udział stacjonarnie.
# Znając liczbę wszystkich zawodników dla każdego miasta oraz liczbę zawodników startujących zdalnie, określ liczbę
# uczniów, którzy biorą udział w zawodach w formie stacjonarnej.
# Wejście
# Wejście składa się z czterech wierszy zawierających dane dotyczące odpowiednio Olsztyna, Torunia, Elbląga i Działdowa.
# W każdym z tych wierszy znajdują się dwie liczby naturalne, z przedziału [1, 250], określające liczbę wszystkich
# uczniów z danego miasta oraz liczbę uczniów z danego miasta startujących zdalnie.
# Wyjście
# Na wyjściu należy wypisać liczbę zawodników, którzy biorą udział w konkursie stacjonarnie.
import sys
try:
    ans = 0
    for _ in range(4):
        inputs = list(map(int, input().split()))
        ans += inputs[0] - inputs[1]
    print(ans)
except:
    sys.exit(0)
