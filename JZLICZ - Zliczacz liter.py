# Koło Młodych Miłośników Łamania Szyfrów pracuje nad odszyfrowaniem pewnego starożytnego manuskryptu. Jądrem systemu
# ma być samouczący się analizator tekstu, a jego pierwszym modułem ma być "zliczacz liter", którego opracowanie
# powierzono Tobie.
# Opracuj program ZLI, który:
# - wczyta ze standardowego wejścia tekst do analizy,
# - dla każdej litery obliczy liczbę jej wystąpień w tekście,
# - wypisze wynik na standardowe wyjście.
# Wejście
# W pierwszym wierszu N - liczba wierszy tekstu do analizy (N ≤ 150). W każdym z następujących N wierszy ciąg złożony
# z maksymalnie 200 znaków spośród małych i wielkich liter alfabetu łacińskiego ('a'..'z', 'A'..'Z') oraz spacji.
# Wyjście
# W kolejnych wierszach litery od 'a' do 'z' i od 'A' do 'Z' w tej kolejności, a po każdej literze spacja i liczba
# wskazująca, ile razy ta litera wystąpiła w tekście.
#
# Uwaga: Pomiń litery, które nie występują w tekście.

lower = [0 for _ in range(26)]
upper = [0 for _ in range(26)]
string = ""
t = int(input())
for _ in range(t):
    string += str(input())
for letter in string:
    if (ord(letter) > 64) and (ord(letter) < 91):
        upper[ord(letter) - 65] += 1
    elif (ord(letter) > 96) and (ord(letter) < 123):
        lower[ord(letter) - 97] += 1
for number in range(26):
    if lower[number] > 0:
        print(chr(number + 97)+" ", lower[number])
for number in range(26):
    if upper[number] > 0:
        print(chr(number + 65)+" ", upper[number])
