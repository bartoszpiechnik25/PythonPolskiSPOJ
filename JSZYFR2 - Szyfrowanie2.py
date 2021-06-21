# Większość kodów wojskowych jest oparta na bardzo dużych liczbach pierwszych. Twoim zadaniem jest złamać kod oparty na
# jakieś liczbie pierwszej z przedziału (120,150). Cały ciąg znaków deszyfruje jedna liczba pierwsza. Każda litera jest
# zaszyfrowana trzy cyfrową liczbą, której reszta z dzielenia przez liczbę deszyfrującą odpowiada wartości znaku w
# tabeli ASCII (bierzemy pod uwagę tylko duże litery A…Z). Jeżeli odczytanie kodu jest nie możliwe wypisuje NIECZYTELNE
# Input
# W pierwszej linii podana jest ilość ciągów t<25, w następnej ilość liter w ciągu s<25, w kolejnej natomiast zestaw
# liczb trzy cyfrowych.
# Output
# Na wyjściu podajemy liczbę, która deszyfruje ciąg oraz odkodowane słowo. Jeżeli odczytanie kodu jest nie możliwe,
# program wypisuje NIECZYTELNE
keys = [127, 131, 137, 139, 149]


def decryption(tab):
    new = ""
    x = []
    for prime_number in keys:
        ans = ""
        for number in tab:
            if (number % prime_number > 64) and (number % prime_number < 91):
                ans += chr(number % prime_number)
            else:
                ans = ""
                break
        if ans != "":
            x.append(prime_number)
            new = ans
    if new == "" or len(x) > 1:
        print("NIECZYTELNE")
    else:
        print(x[0], new)


t = int(input())
for _ in range(t):
    z = int(input())
    A = list(map(int, input().split()))
    decryption(A)
