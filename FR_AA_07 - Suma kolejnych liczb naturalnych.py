# Małgosia dodała do siebie k kolejnych liczb naturalnych i otrzymała sumę n. Jasiu otrzymał od Małgosi dwie
# wartości - k i n i teraz ma odgadnąć k kolejnych liczb naturalnych, które sumują się do n. Pomóż Jasiowi!
# Wejście
# W pierwszym wierszu wejścia znajdują się dwie liczby całkowite k, n (1 ≤ k ≤ n ≤ 109).
# Wyjście
# W pierwszym i jedynym wierszu wyjścia należy wypisać w porządku rosnącym k kolejnych liczb naturalnych, które sumują
# się do liczby n.
# Uwaga! Wartości k i n z wejścia są tak dobrane, że istnieje taki ciąg k kolejnych liczb naturalnych, których suma
# wynosi n.
import sys
try:
    inputs = list(map(int, input().split()))
    first = int(inputs[1]/inputs[0] + (1 - inputs[0]) / 2)
    print(*[i for i in range(first, first + inputs[0])])
except:
    sys.exit(0)
