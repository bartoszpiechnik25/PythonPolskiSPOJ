# Napisz program, który sprawdza, czy istnieje trójkąt o bokach o podanej długości.
# Wejście
# Na wejście programu podana zostanie pewna nieokreślona liczba zestawów danych. Każdy z zestawów składa się z 3 liczb
# rozdzielonych spacjami. Poszczególne zestawy zostaną rozdzielone znakiem nowej linii.
# Wyjście
# Na wyjściu ma się pojawić ciąg binarny, którego i-ty wyraz jest równy 1, jeżeli istnieje trójkąt o długościach boków
# podanych w i-tym wczytanym z wejścia zestawie. Poszczególne elementy tego ciągu należy rozdzielić znakiem nowej linii.

import sys

def triangle_inequality(a, b, c):
    if  a < b + c and b < a + c and c < a + b:
        return 1
    else:
        return 0
try:
    while True:
        x, y, z = map(float, input().split())
        if x != '' and y != '' and z != '':
            print(triangle_inequality(x, y, z))
        else:
            break
except:
    sys.exit(0)