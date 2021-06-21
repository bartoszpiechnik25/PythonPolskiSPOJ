# Dany jest ciąg xn określony rekurencyjnie:
# x0=s,
# xn+1=3*xn+1, jeśli xn jest nieparzyste i
# xn+1=xn/2, jeśli xn jest parzyste
# Napisz program, który oblicza pierwsze takie n, dla którego xn=1.
# Wejście
# W pierwszej linii liczba testów t. W każdym z t kolejnych wierszy jedna liczba całkowita s, 1 <= s <= 10000.
# Wyjście
# W każdej linii jedna liczba - obliczona wartość n.


def first_n(x, n):
    if x == 1:
        return n
    elif x == 0:
        return 0
    elif x % 2 != 0:
        return first_n(3 * x + 1, n=n+1)
    else:
        return first_n(x / 2, n=n+1)


for _ in range(int(input())):
    result = 0
    print(first_n(int(input()), result))
