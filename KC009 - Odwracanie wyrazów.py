# Napisz program, który zapisuje wspak podane na wejściu wyrazy.
# Wejście
# Na wejście programu podana zostanie pewna nieokreślona ilość wyrazów, tj. ciągów znaków zbudowanych z małych liter.
# Poszczególne wyrazy zostaną rozdzielone znakiem nowej linii. Przyjmujemy, że długość wyrazów nie przekracza 1000 znaków.
# Wyjście
# Na wyjściu mają się pojawić te same wyrazy, które pojawiły się na wejściu, ale zapisane wspak. Poszczególne wyrazy
# należy rozdzielić znakiem nowej linii.


import sys

def reverse(string):
    n = len(string)
    ans = ""
    for i in range(1, n + 1):
        ans += string[-i]
    print(ans)

for line in sys.stdin:
    reverse(line)