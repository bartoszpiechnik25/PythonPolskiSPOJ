# Napisz program, który sumuje pojawiające się na wejściu liczby całkowite.
# Wejście
# Na wejście programu podana zostanie pewna nieokreślona ilość zestawów danych. Pojedynczy zestaw składa się z ciągu
# liczb całkowitych, rozdzielonych spacjami i kończących się zerem. Poszczególne zestawy zostaną rozdzielone znakiem
# nowej linii.
# Wyjście
# Na wyjściu mają się pojawić sumy liczb z poszczególnych zestawów danych. Ich wartości należy rozdzielić znakami nowej
# linii. Na samym końcu należy dodatkowo podać sumę wszystkich wczytanych z wejścia liczb (jest ona mniejsza niż 1015).
import sys

try:
    ans = 0
    for user_input in sys.stdin:
        inputs = list(map(int, user_input.split()))
        print(sum(inputs))
        ans += sum(inputs)
    print(ans)
except:
    sys.exit(0)