# Wejście
# Najpierw liczba testów t (t ≤ 100). Następnie dla każdego testu liczba n (n ≤ 100) i n liczb oddzielonych spacjami.
# Wyjście
# Dla każdego testu n liczb w porządku odwrotnym niż na wejściu.

t = int(input())

for _ in range(t):
    a = list(map(int, input().split()))
    print(*a[:0:-1])
