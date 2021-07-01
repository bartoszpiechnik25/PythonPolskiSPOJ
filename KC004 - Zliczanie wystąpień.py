# Napisz program, który sprawdza, ile razy dana liczba całkowita wystąpiła w danym ciągu.
# Wejście
# Na wejście programu podana zostanie pewna nieokreślona liczba zestawów danych. Każdy z zestawów składa się z trzech
# rozdzielonych spacjami części: poszukiwanej liczby całkowitej, długości przeszukiwanego ciągu oraz samego ciągu.
# Poszczególne liczby w ciągu zostały rozdzielone spacjami; zestawy odseparowano od siebie znakiem nowej linii.
# Wyjście
# Na wyjściu ma się pojawić ciąg liczbowy, którego i-ty wyraz jest równy ilości wystąpień liczby podanej w pierwszej
# części i-tego wczytanego z wejścia zestawu w ciągu stanowiącym trzecią część tego zestawu. Poszczególne elementy tego
# ciągu należy rozdzielić znakiem nowej linii.

import sys

try:
    for line in sys.stdin:
        inputs = list(map(int, line.split()))
        count = 0
        for number in inputs[2:]:
            if number == inputs[0]:
                count += 1
        print(count)
except:
    sys.exit(0)
