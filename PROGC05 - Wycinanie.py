# Dla podanego wyrazu oraz podanej litery należy przepisać wyraz na wejście z pominięciem tej wskazanej litery.
# Wejście
# Dane wejściowe składają się z wielu linii. Każda linia ma następujący format:
# c wyraz
# gdzie c jest małą literą (a,...,z), natomiast wyraz jest napisem złożonym (również z liter a,....,z) o długości
# nie przekraczającej 100 znaków.
# wyjście
# Dla każdej linii wejściowej należy (w osobnej linii) przepisać na wyjście wyraz pomijając w nim litery równe c
import sys

for char in sys.stdin:
    ans = ""
    for i in range(len(char)):
        if char[i] == char[0] or char[i] == " ":
            continue
        else:
            ans += char[i]
    print(ans)
