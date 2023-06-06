# funkcja zagnieżdzona

def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2  # bez nawiasów, bo chcemy tylko odesłać referencje do funkcji


xFun = fun1()  # To jest fun1
print(xFun)  # <function fun1.<locals>.fun2 at 0x102b31a80>
print(type(xFun))  # <class 'function'>
xFun()  # To jest fun2
