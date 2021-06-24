# Szyfr Cezara jest to szyfr za pomocą, którego Juliusz Cezar szyfrował swoje listy do Cycerona. Jako ciekawostkę można
# podać, że szyfr ten był podobno używany jeszcze w 1915 roku w armii rosyjskiej, gdyż tylko tak prosty szyfr wydawał
# się zrozumiały dla sztabowców.
# Każdą literę tekstu jawnego zamieniamy na literę przesuniętą o 3 miejsca w prawo. I tak literę A szyfrujemy jako
# literę D, literę B jako E itd. W przypadku litery Z wybieramy literę C. W celu odszyfrowania tekstu powtarzamy
# operację tym razem przesuwając litery o 3 pozycje w lewo.
# Input
# Na wejściu pojawi się tekst zawierający jedynie wielkie litery alfabetu łacińskiego, spacje oraz znaki nowej linii,
# a jego długość nie przekracza 200 znaków.
# Output
# Na wyjściu otrzymujemy zaszyfrowany tekst używając Szyfru Cezara.
while True:
    s = str(input())
    if s != "":
        ans = ""
        for char in s:
            if char == " " or char == "\n":
                ans += char
            elif ord(char) == 88:
                ans += "A"
            elif ord(char) == 89:
                ans += "B"
            elif ord(char) == 90:
                ans += "C"
            else:
                ans += chr(ord(char) + 3)
        print(ans)
    else:
        break
