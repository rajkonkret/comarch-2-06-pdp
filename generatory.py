def kwadrat(n):
    for x in range(n):
        print(x ** 2)


def kwa2(n):
    for x in range(n):
        yield x ** 2  # zwraca wynik i zapamietuje w ktorym miejscu sie zatrzymał


kwadrat(5)  # 0..4 liczy kwadraty
kwa = kwa2(5)
print(kwa)  # <generator object kwa2 at 0x104e0f510>
print(next(kwa))
print(next(kwa))
print(next(kwa))  # 4
print("wypisac cokolwiek")
print("zrobic cokolwiek")
lista = []
lista.append(4)
print(next(kwa))  # 9
print(next(kwa))  # 16
kwa_2 = kwa2(9)
print(next(kwa_2))
print(next(kwa_2))
print(next(kwa_2))
print(next(kwa_2))  # 9
# 13:20
