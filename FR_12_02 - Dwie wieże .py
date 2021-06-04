# Napisz program, który sprawdzi, czy dwie wieże ustawione na szachownicy wzajemnie się atakują.
# Wejście
# W pierwszym i jedynym wierszu wejścia znajdują się dwie różne współrzędne pól szachownicy z przedziału [a1 - h8],
# na których ustawione są dwie wieże.
# Wyjaśnienie:
# Współrzędne definiowane są za pomocą kombinacji liter i liczb. Kolumny szachownicy oznaczone są małymi literami od a
# do h, a wiersze ponumerowane są od 1 do 8. Wieża porusza się po liniach pionowych i poziomych, w dowolnym kierunku
# i o dowolną liczbę niezajętych pól. W tym problemie dwie wieże atakują się wzajemnie, gdy znajdują się w tym samym
# wierszu lub tej samej kolumnie.
# Wyjście:
# Na wyjściu należy wypisać słowo TAK, jeśli wieże wzajemnie się atakują, w przeciwnym przypadku należy wypisać słowo NIE.

wsp = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}


def rook_move(coordinates):
    ans = []
    ans.append(int(coordinates[1]) - 1)
    ans.append(wsp[coordinates[0]])
    return ans


a, b = map(str, input().split())
rook_1 = rook_move(coordinates=a)
rook_2 = rook_move(coordinates=b)
if rook_1[0] == rook_2[0] or rook_1[1] == rook_2[1]:
    print("TAK")
else:
    print("NIE")
