# Nauczycielka matematyki obiecała przepytać Jasia z dodawania dwóch dowolnych liczb naturalnych. Niestety Jaś nie
# umiał dodawać, więc umówił się z kolegą, który miał kalkulator, że będzie mu podpowiadał. Na pierwsze i drugie
# pytanie pani Jaś przy pomocy kolegi podał odpowiedź. Pani szybko się zorientowała w oszustwie. Chcąc ukarać obu
# uczniów zadała im zadanie dodania dwóch bardzo dużych liczb, które na pewno nie mieszczą się na wyświetlaczu
# kalkulatora.
# Twoim zadaniem jest napisać program dodający dwie bardzo duże liczby naturalne.
# Input
# Na wejściu w pierwszej linii zostaje podana liczba naturalna t, t nalezy do przedzialu 1..100, będącą ilością par
# liczb naturalnych, które należy dodać. W kolejnych wierszach t podane zostaną dwie liczby naturalne o maksymalnie
# 1000 cyfr, liczby oddzielone są spacją.
# Output
# Na wyjściu wydrukowana powinna być w każdym wierszu liczba naturalna, która jest wynikiem dodawania dwóch liczb
# naturalnych podanych na wejściu w odpowiednim wierszu.

t = int(input())

for i in range(t):
    a = list(map(int, input().split()))
    print(sum(a))
