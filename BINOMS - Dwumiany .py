# Dla liczb całkowitych n i k, 0 <= k <= n <= 1000, wyznacz liczbę różnych k-elementowych podzbiorów zbioru
# n-elementowego. Liczby n i k będą dobrane tak, aby wynik nie przekroczył 1 000 000 000.
# Input
# T [ liczba testów, T <= 10000 ]
# n_1 k_1
# n_2 k_2
# ...
# n_T k_T
# Output
# wynik_1
# wynik_2
# ...
# wynik_T

def dwumian(n, k):
    if n == 0 or k == 0:
        return 1
    else:
        a, b = 1, 1
        for i in range(n - k + 1, n + 1):
            a *= i
        for j in range(1, k + 1):
            b *= j
        return a // b

T = int(input())
for i in range(T):
    x , y = map(int, input().split())
    print(dwumian(x,y))