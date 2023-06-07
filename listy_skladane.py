numbers = [1, 2, 3, 4, 5]

# Tworzenie nowej listy
squared = [num ** 2 for num in numbers]
print(squared)  # [1, 4, 9, 16, 25]

# for num in numbers:
#     jakaslista.append(num ** 2)

even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)  # [2, 4]

modifed_numbers = [num * 2 if num % 2 == 0 else num for num in numbers]
print(modifed_numbers)  # [1, 4, 3, 8, 5]

even_odd = ['parzysta' if x % 2 == 0 else 'nieparzysta' for x in numbers]
print(even_odd)  # ['nieparzysta', 'parzysta', 'nieparzysta', 'parzysta', 'nieparzysta']

squared_numbers = [x ** 2 for x in range(1, 6)]  # 1..5
print(squared_numbers)  # [1, 4, 9, 16, 25]

# abs() - wartośc absolutna - wartosc bez znaku
numbers2 = [-1, -2, 3, -4, 5]
absolute = [abs(x) for x in numbers2]
print(absolute)  # [1, 2, 3, 4, 5]

word = "Python"
print(list(word))  # ['P', 'y', 't', 'h', 'o', 'n']

# lista1 = [word] - odpowiednik list1.append(word)
lista1 = [word]  # tworzenie listy z elementów w zmiennej, ['Python']
print(lista1)  # ['Python']

letters = [letter for letter in word]
print(letters)  # ['P', 'y', 't', 'h', 'o', 'n']
# 11:25