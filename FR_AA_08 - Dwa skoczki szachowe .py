# Napisz program, który sprawdzi, czy dwa skoczki szachowe ustawione na szachownicy wzajemnie się atakują.
# Wejście:
# W pierwszym i jedynym wierszu wejścia znajdują się dwie różne współrzędne pól szachownicy z przedziału [a1 - h8]
# , na których ustawione są dwa skoczki szachowe.
# Wyjaśnienie:
# Współrzędne definiowane są za pomocą kombinacji liter i liczb. Kolumny szachownicy oznaczone są małymi literami od a
# do h, a wiersze ponumerowane są od 1 do 8.
# Skoczek porusza się o jedno pole do przodu (w pionie lub poziomie), po czym o jedno pole na ukos w dowolnym kierunku.
# Rysunek poniżej przedstawia wszystkie możliwe ruchy skoczka znajdującego się na polu d5.
# Dwa skoczki szachowe atakują się wzajemnie, gdy wzajemnie znajdują się na polach, na które mogą wykonać ruch.
# Wyjście:
# Na wyjściu należy wypisać słowo TAK, jeśli skoczki szachowe wzajemnie się atakują. W przeciwnym przypadku należy
# wypisać słowo NIE.
wsp = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}


def knight_place(co_ordinates):
    if co_ordinates[0] in wsp:
        a = wsp[co_ordinates[0]]
        b = int(co_ordinates[1]) - 1
        return b, a


x, y = map(str, input().split())

knight_1 = knight_place(co_ordinates=x)
knight_2 = knight_place(co_ordinates=y)

if (knight_1[0] - knight_2[0]) ** 2 + (knight_1[1] - knight_2[1]) ** 2 == 5:
    print("TAK")
else:
    print("NIE")
