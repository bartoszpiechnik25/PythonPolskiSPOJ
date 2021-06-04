# Jasio wie, że sekretny kod na którym mu zależy jest nieujemną całkowitą liczbą n cyfrową. Kłopot w tym, że poznał
# tylko niektóre jej cyfry. Teraz nie wie, czy ma tracić czas na próbowanie wszystkich możliwych kodów, czy też potrwa
# to za długo i powinien jeszcze dokładniej poznać tę liczbę.
# Wejście
# W pierwszej linii wejścia znajduje się liczba testów 0<t<=1000. Następnie każdy test w oddzielnej linii. Pojedynczy
# test składa się z liczby 0<n<=100 oraz, po spacji, ciągu n znaków z których każdy jest cyfrą, jeśli Jasio wie że w
# kodzie na danym miejscu stoi ta cyfra, lub znakiem zapytania, jeśli Jasio nie wie jaka cyfra stoi na danym miejscu
# w jego kodzie.
# Wyjście
# Dla każdego testu wynik w osobnej linii. Wynikiem jest liczba możliwych sekretnych kodów.

import sys

t = int(input())

for i in range(t):
    x, y = map(str, input().split())
    ans = 1
    x = int(x)
    if x > 100 or x < 0:
        sys.exit(0)
    else:
        if len(y) == 1 and y =="?":
            print(ans * 10)
        else:
            for j in range(x):
                if y[j] == "?":
                    if j == 0:
                        ans *= 9
                    else:
                        ans *= 10
            print(ans)
