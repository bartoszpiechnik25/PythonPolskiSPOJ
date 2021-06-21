# Napisz program, który oblicza sumę pojawiających się na wejściu liczb.
# Wejście
# Na wejście programu podana zostanie pewna nieokreślona, ale niewielka ilość małych liczb całkowitych
# (z zakresu -100..100). Poszczególne liczby zostaną rozdzielone znakiem nowej linii.
# Wyjście
# Na wyjściu ma się pojawić ciąg liczbowy, którego i-ta pozycja jest równa sumie i pierwszych wczytanych z wejścia
# liczb. Poszczególne liczby należy rozdzielić znakami nowej linii.
import sys
a = []
for number in sys.stdin:
    a.append(int(number))
    print(sum(a))
