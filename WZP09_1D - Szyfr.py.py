# Napisz program, który odkoduje zaszyfrowany tekst. Algorytm szyfrowania jest następujący: dla tekstu o długości n
# znaków (gdzie kolejne znaki mają indeksy od 1 do n) wyznaczamy element środkowy o indeksie (n + 1) div1 2 i przesuwamy
# go na początek tekstu. Operację tę powtarzamy rekurencyjnie dla tekstu z prawej i z lewej strony środkowego znaku. Oto
# schemat działania algorytmu szyfrowania dla słowa „ALGORYTM”:
# Wyznaczamy środkowy element: (8 + 1) div 2 = 4
# ALG-O-RYTM
# Przestawiamy środkowy element na początek tekstu:
# O-ALG-RYTM
# Powtarzamy pierwsze dwa punkty dla tekstu, który na początku znajdował się po lewej stronie litery O:
# O-L-A-G-RYTM
# To samo robimy dla tekstu z prawej strony litery O:
# O-L-A-G-Y-R-TM
# Ponieważ tekst jest podzielony na fragmenty krótsze niż 3 znaki to nie mamy już czego przestawiać. Zakodowana postać
# słowa „ALGORYTM” to „OLAGYRTM”.
# Wejście
# W pierwszej i jedynej linii wejścia znajduje się zaszyfrowany tekst, którego długość nie przekroczy 10000 znaków.
# Tekst może zawierać wielkie i małe litery alfabetu angielskiego, spacje oraz znaki interpunkcyjne.
# Wyjście
# Na wyjściu należy wypisać tekst w postaci odszyfrowanej.


def decryption(string):
    n = len(string)
    mid = (n + 1) // 2
    if n < 3:
        return string
    else:
        a = string[0]
        new = string[1:mid]
        b = string[mid:]
        return decryption(new) + a + decryption(b)



print(decryption(str(input())))