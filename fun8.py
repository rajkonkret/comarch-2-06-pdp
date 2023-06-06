def allparams(a, b, /, c=42, *args, d=256, **kwargs):
    print(f"a={a}, b={b}")
    print(f"c={c}, d={d}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")


allparams(1, 2)  # a=1, b=2
# allparams(b=2, a=1)  # TypeError: allparams() missing 2 required positional arguments: 'a' and 'b'
# ? - oddziele arumenty pozycyjne od tych co moga byc podane po nazwie
allparams(1, 2, c=9)
allparams(1, 2, 9, 1, 2, 3, 4, 5, 56)  # c jako trzecia pozycja
allparams(1, 2, 3, 4, 5, 6, 7, 8, d=100)  # d musi zostać podane jawnie jako nazwa d=100
allparams(1, 2, 3, 4, 5, 6, 7, 8, d=100, radek="/")  # kwargs={'radek': '/'}
allparams(1, 2, 3, 4, 5, 6, 7, 8, d=100, radek="/", a=1, b=17)  # kwargs={'radek': '/', 'a': 1, 'b': 17}
