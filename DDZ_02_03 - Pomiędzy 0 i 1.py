# Wypisz wszystkie cyfry znajdujące się między pierwszym wystąpieniem cyfry 0 i ostatnim wystąpieniem cyfry 1.
# Wejście
# W pierwszym wierszu jedna liczba złożona z maksymalnie miliona cyfr i nie mniej niż 3 cyfry.
# Za zerem jest zawsze co najmniej jedna jedynka.
# Wyjście
# Ciąg cyfr występujący między pierszym wystąpieniem cyfry 0 i ostatnim wystąpieniem cyfry 1. Jeśli ciąg jest pusty,
# to należy wypisać napis PUSTY.
import sys
try:
    number = str(input())
    i = 0
    k = -1
    while True:
        if number[i] != "0":
            i += 1
        if number[k] != "1":
            k -= 1
        if number[i] == "0" and number[k] == "1":
            break
    ans = "".join(number[i + 1:k])
    if len(ans) == 0:
        print("PUSTY")
    else:
        print(ans)
except:
    sys.exit(0)
