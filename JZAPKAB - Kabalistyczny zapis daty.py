# Istnieje bardzo łatwy sposób zapisu daty. Ten typowo barokowy pomysł nawiązywał do kabały, w której literom
# hebrajskim przypisane były liczby. W tym wypadku litery alfabetu łacińskiego odpowiadały następującym liczbom:
# Datę oblicza się sumując wszystkie liczby odpowiadające kolejnym literom tekstu. Zapis stosowano w drukach
# i rękopisach. W przypadku druków najczęściej podawano pod poszczególnymi słowami sumę liczb ich liter. Autorzy
# trudzili się nad stworzeniem tekstu, z którego daje się odczytać datę.
# Input
# Na wejściu podany jest wyraz, pisany małymi literami (używając wyłącznie liter podanych powyżej). Wyraz nie większy
# niż 25 znaków.

letters = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "k": 10, "l": 20, "m": 30, "n": 40,
        "o": 50, "p": 60, "q": 70, "r": 80, "s": 90, "t": 100, "v": 200, "x": 300, "y": 400, "z": 500}
s = str(input())
date = 0
for char in s:
    date += letters[char]
print(date)
