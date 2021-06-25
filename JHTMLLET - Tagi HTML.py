# Często się zdarza, że pisząc stronę internetową piszemy tagi HTMLowe w postaci dużych, a czasami małych liter.
# Powoduje, że kod strony wygląda nieestetycznie. Twoim zadanie jest napisanie programu, który przerobi wszystkie tagi
# HTMLowe na duże litery, tzn, wszystkie litery pomiędzy znakami "<" a ">" zamieni na duże litery.
# Input
# Na wejściu znajduje się fragment kodu HTMLowego.
# Output
# Na wyjściu znajduje się kod HTML z wejścia, tyle tylko, że wszystkie tagi HTMLowe składają się z dużych liter.

import sys

text = []

for line in sys.stdin:
    if line == "":
        break
    else:
        text.append(line)

ans = ""

for i in range(len(text)):
    char = 0
    while char < len(text[i]):
        if text[i][char] == "<":
            ans += text[i][char]
            while text[i][char] != ">":
                char += 1
                ans += text[i][char].upper()
        else:
            ans += text[i][char]
        char += 1
    ans += '\n'

print(ans)
