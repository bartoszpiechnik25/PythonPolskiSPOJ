# Dla zadanej liczby n, wypisz ostatnia niezerową cyfrę liczby n!
# Wejście
# W pierwszej linijce znajduje się liczba testów t (1<=t<=1000), w każdej następnej linijce znajduje się dokładnie
# jedna liczba całkowita n(1<=n<=1000).
# Wyjscie
# Dla każdego n należy wyświetlić ostatnia niezerową cyfrę liczby n!.


dig = [1, 1, 2, 6, 4, 2, 2, 4, 2, 8]

t = int(input())


def lastNon0Digit(n):
    if (n < 10):
        return dig[n]
    if (((n // 10) % 10) % 2 == 0):
        return (6 * lastNon0Digit(n // 5) * dig[n % 10]) % 10
    else:
        return (4 * lastNon0Digit(n // 5) * dig[n % 10]) % 10
    return 0


for _ in range(t):
    x = int(input())
    print(lastNon0Digit(x))

