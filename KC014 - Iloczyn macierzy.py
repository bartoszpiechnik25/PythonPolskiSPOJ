# Napisz program, który wyznacza iloczyn podanych macierzy kwadratowych.
# Wejście
# Na wejście programu podana zostanie pewna ilość zestawów danych. Każdy zestaw będzie się składać z trzech linii.
# Pierwsza linia będzie zawierać liczbę z zakresu 1-10 (wymiar macierzy). Druga i trzecia będą zawierać rozdzielone
# spacją elementy macierzy, które mają zostać pomnożone. Elementy macierzy A wymiaru n na n zostaną podane w kolejności
# A[1,1], A[1,2], ..., A[1,n], A[2,1], A[2,2], ..., A[2,n], ..., A[n,1], A[n,2], ..., A[n,n]. Przyjmujemy, że elementy
# macierzy są liczbami naturalnymi z zakresu 0-1000.
# Wyjście
# Na wyjściu mają się pojawić macierze będące iloczynami wczytanych z wejścia macierzy. Elementy macierzy należy wypisać
# w tej samej kolejności, jak w danych wejściowych. Poszczególne macierze należy rozdzielić znakami nowej linii.

import sys


def linear_matrix_rep_multiply(matrix_1, matrix_2, n):
    ans = []
    for i in range(n):
        for j in range(n):
            total = 0
            for k in range(n):
                total += matrix_1[k + i * n] * matrix_2[k * n + j]
            ans.append(total)
    return ans


for line in sys.stdin:
    n = int(line)
    arr_1 = list(map(int, input().split()))
    arr_2 = list(map(int, input().split()))
    print(*linear_matrix_rep_multiply(arr_1, arr_2, n))
