# funkcja do obliczania średniej

def liczby(c, *cyfry):
    suma = 0
    print(c, cyfry)
    print(type(cyfry))  # <class 'tuple'>
    try:
        for cy in cyfry:
            print(cy)
            suma += cy
        print(f"Suma {suma}")
        count = len(cyfry)

        print(f"Średnia wynosi {suma / count}")
    except Exception as e:
        print("Bład", e)


liczby(c=9)
liczby(1)
liczby(1, 2, 3, 4, 5)
liczby(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 2, 678, 3534, 5334, 6544, 3443, )
liczby(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 2, 678, 3534, 5334, 6544, 3443, "A")
