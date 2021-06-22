# Przesuń elementy tablicy cyklicznie w lewo o zadaną liczbę miejsc.
# Input
# Najpierw dwie liczby n i k takie, że 1 < k < n < 10000, a następnie w kolejnym wierszu n liczb.
# Output
# W jednym wierszu n liczb w zmienionym porządku (przesuniętych cyklicznie o k miejsc).
x, k = map(int, input().split())
ans = list(map(int, input().split()))
for i in range(k):
    ans += [ans.pop(0)]
print(*ans)
