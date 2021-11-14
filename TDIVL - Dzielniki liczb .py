# Dla zadanej pary liczb całkowitych a oraz b takich, że 1 <= b <= a <= 101000 należy odpowiedzieć na pytanie czy b
# jest dzielnikiem a, tzn. czy istnieje taka liczba c, że a = b * c.
# Wejście
# W pierwszej linii na wejściu podana została liczba zestawów testowych t <= 100. W kolejnych t liniach podane zostały
# pary liczb a b.
# Wyjście
# Dla każdego testu (pary liczb) należy wydrukować odpowiedź TAK lub NIE, w zależności od tego czy liczba b jest
# dzielnikiem liczby a czy nie jest.
# Zestawy testowe
# Dane wejściowe składają się z trzech zestawów testowych:
# pierwszy zestaw (za 5 pkt) zawiera liczby o wartościach z zakresu od 0 do 1012,
# drugi zestaw (za 5 pkt) zawiera liczby o wartościach z zakresu od 0 do 10100 o ilorazie nie przekraczającym 10000,
# trzeci zestaw (za 10 pkt) zawiera dowolne liczby z zakresu od 0 do 101000.
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        if a % b == 0:
            print("TAK")
        else:
            print("NIE")
