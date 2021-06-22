# Wejście
# Najpierw liczba testów t (t ≤ 100). Następnie dla każdego testu liczba n (1 < n ≤ 100) i n liczb.
# Wyjście
# Dla każdego testu n liczb w zmienionym porządku.
t = int(input())
for _ in range(t):
    rol = list(map(int, input().split()))
    rol += [rol.pop(1)]
    print(*rol[1:])
