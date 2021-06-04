# Dla podanej liczby n wypisz nty wiersz trójkąta Pascala.
# 1 - zerowa linia
# 1 1 - pierwsza linia
# 1 2 1 - druga linia
# 1 3 3 1 - trzecia linia
# 1 4 6 4 1 - czwarta linia
# Input:
# Pierwsza linia zawiera liczbę testów t. W kolejnych t liniach znajduje się liczba naturalna n (0<=n<101).
# Output:
# Dla każdego testu jedna linia - nty wiersz z trójkąta Pascala.

def factorial(n):
    if n < 2 :
        return 1
    else:
        return n * factorial(n - 1)

def pascals_triangle(n):
    tab = []
    if n < 0 or n > 100:
        return None
    if n < 1:
        tab.append(1)
    else:
        for i in range(n + 1):
            if i == 0 or i == n:
                tab.append(1)
            else:
                a = int(factorial(n) // (factorial(i) * factorial(n - i)))
                tab.append(a)
    print(*tab)

t = int(input())

for i in range(t):
    n = int(input())
    pascals_triangle(n)
