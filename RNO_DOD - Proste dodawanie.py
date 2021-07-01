# Twoim zadaniem jest dodać wszystkie liczby całkowite podane na wejściu.
# Wejście
# W pierwszym wierszu znajduje się liczba t testów (0 < t < 100) Każdy test opisany jest w następujący sposób.
# W pierwszym wierszu dana jest liczba n - liczba liczb do zsumowania. Następnie podanych jest n liczb pooddzielanych
# spacją.
import sys
try:
    t = int(input())

    for _ in range(t):
        x = int(input())
        inputs = list(map(int, input().split()))
        print(sum(inputs))
except:
    sys.exit(0)
