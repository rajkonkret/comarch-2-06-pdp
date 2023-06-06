# match case
lista = []

lang = input("Podaj znany Ci język programowania")

match lang:
    case "python":
        lista.append(lang)
    case "java":
        lista.append(lang)
    case _:  # wartośc domyslna
        print("Nie znam takiego języka")

print(lista)
