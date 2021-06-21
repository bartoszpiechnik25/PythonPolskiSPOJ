# Input
# W pierwszej linii liczba testów t, w kolejnych liniach po dwie liczby w każdym wierszu.
# Output
# W każdej linii jedna liczba - wynik działania funkcji nwd
def nwd(a, b):
    if b == 0:
        return a
    else:
        c = a % b
        return nwd(b, c)


t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    print(nwd(x, y))
