# Dane są: okrąg o środku o=(xo, yo) i promieniu r oraz n punktów pi=(xi, yi). Dla każdego punktu pi sprawdź, jego
# położenie względem okręgu o.
# Wejście
# W pierwszej linii 3 liczby całkowite z przedziału [-10000, 10000] będące współrzędnymi środka okręgu i jego
# promieniem.
# Następnie n - liczba punktów i w kolejnych n liniach po dwie liczby całkowite będące współrzędnymi kolejnego punktu.
# Wyjście
# Dla każdego punktu w osobnej linii jedna litera:
# I, jeśli punkt leży w obszarze wewnętrznym okręgu
# O, jeśli punkt leży w obszarze zewnętrznym okręgu
# E, jeśli punkt leży na okręgu


x, y, r = map(int, input().split())


def where_in_circle():
    user_x, user_y = map(int, input().split())
    if ((x - user_x) * (x - user_x) + (y - user_y) * (y - user_y) == r * r):
        print("E")
    elif ((x - user_x) * (x - user_x) + (y - user_y) * (y - user_y) > r * r):
        print("O")
    else:
        print("I")


n = int(input())

while n > 0:
    where_in_circle()
    n -= 1
