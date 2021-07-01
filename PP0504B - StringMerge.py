# Napisz funkcję:
# która sklei ze sobą dwa łańcuchy biorąc na przemian po jednym znaku z każdego łańcucha i umieści w nowej dynamicznie
# alokowanej tablicy znaków, do której zwróci wskaźnik. Należy wziąć po tyle znaków ile jest w krótszym łańcuchu.
# Input
# W pierwszej linii liczba testów t, w kolejnych liniach po dwa łańcuchy znaków odzielone spacją.
# Output
# W każdej linii jeden łańcuch, wynik działania funkcji string_merge.
import sys
try:
    t = int(input())

    for _ in range(t):
        inputs = list(map(str, input().split()))
        tab = []
        for i in range(len(inputs[0]) if len(inputs[0]) < len(inputs[1]) else len(inputs[1])):
            tab.append(inputs[0][i])
            tab.append(inputs[1][i])
        ans = "".join(tab)
        print(ans)
except:
    sys.exit(0)

