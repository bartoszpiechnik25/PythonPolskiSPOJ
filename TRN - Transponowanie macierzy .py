# Transponuj podaną macierz.
# Wejście:
# W pierwszym wierszu znajdują się dwie liczby m n(1 <= m, n <= 200) oznaczające odpowiednio liczbę wierszy oraz liczbę
# kolumn.Następnie następuje m wierszy, w każdym n liczb.
# Wyjście:
# Na wyjściu powinna znaleźć się macierz transponowana do zadanej.

m, n = map(int, input().split())
tab = []
for i in range(m):
    tab.append(list(map(int, input().split())))
print(tab)
ans = []
for j in range(n):
    for k in range(m):
        print(tab[k][j], end=" ")
    print()