# Jest rok 2005. Jasiowi udało się przekonać kilku kolegów, aby przesłali mu swoje pliki config.dat programu Gadu Gadu.
# Teraz, po znalezieniu potrzebnych informacji w Internecie, jest już gotowy do napisania własnego programu
# deszyfrującego... i w ten sposób będzie miał hasła dostępu do kont gadu gadu kolegów...
# Input
# Na wejściu podana jest pewna liczba danych testowych. Każdy zestaw znajduje się w osobnej linii i składa się z 20
# wielkich liter (A-P) stanowiących zaszyfrowane hasło do konta Gadu-Gadu.
# Output
# Na wyjściu wypisz hasła w odkodowanej postaci.

import sys

first = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12,
         "N": 13, "O": 14,"P": 15}
second = {"A": 0, "B": 16, "C": 32, "D": 48, "E": 64, "F": 80, "G": 96, "H": 112, "I": 128, "J": 144, "K" :160,
          "L": 176, "M": 192, "N": 208, "O": 224, "P": 240}

def gg_decryption(encrypted):
    ans = ""
    n = len(encrypted)
    for i in range(0, n, 2):
        ans += chr(first[encrypted[i]]+ second[encrypted[i + 1]])
    return ans

for line in sys.stdin:
    line = str(line[:20])
    print(gg_decryption(line))
