# Przepisz dane z wejścia na wyjście. Dane wejściowe są dwucyfrowymi liczbami naturalnymi. Zakończ działanie programu,
# gdy na wejściu pojawi się, trzecia liczba 42 poprzedzona jakąkolwiek inną liczbą, różną od 42.
# Wejście
# W każdej linii jedna liczba dwucyfrowa.
# Wyjście
# W każdej linii jedna liczba dwucyfrowa. Odczytane wartości 42 również powinny się pojawić.
first = True
past = 0
count = 0
while True:
    x = int(input())
    print(x)
    if x == 42 and past != 42 and not first:
        count += 1
    if count == 3:
        break
    past = x
    first = False
