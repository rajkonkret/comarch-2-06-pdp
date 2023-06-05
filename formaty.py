user = "Tomek"  # str
wiek = 39  # int
wersja = 3.90000001  # float - zmiennoprzecinkowy
liczba = 134632344532  # int

print("Witaj %s masz teraz %d lat" % (user, wiek))

print("Witaj %(user)s masz teraz %(wiek)d lat" % {'user': user, 'wiek': wiek})
# Witaj Tomek masz teraz 39 lat
print("Witaj {} masz teraz {} lat".format(user, wiek))
print("Witaj {} masz teraz {} lat".format(wiek, user))  # dziąla w sensie pythona, nie działa w sensie logicznym
print(f"Witaj {user} masz teraz {wiek} lat")  # fstring

print("Używamy wersji Python %i" % 3)  # Używamy wersji Python 3
print("Używamy wersji Python %f" % 3.9)  # Używamy wersji Python 3.900000
print("Używamy wersji Python %.1f" % 3.9)  # Używamy wersji Python 3.9
print("Używamy wersji Python %.2f" % 3.9)  # Używamy wersji Python 3.90
print("Używamy wersji Python %.f" % 3.9)  # Używamy wersji Python 4
print("Używamy wersji Python %.0f" % 3.9)  # Używamy wersji Python 4
print("Używamy wersji {} Pythona".format(wersja))

print(f"Uzywamy wersji {wersja}")
print(f"Uzywamy wersji {wersja:.1f}")  # Uzywamy wersji 3.9
print(f"Uzywamy wersji {wersja:.2f}")  # Uzywamy wersji 3.90
print(f"Uzywamy wersji {wersja:.0f}")  # Uzywamy wersji 4

print(f"{user:>20}")  # "               Tomek"
print(f"{user:>10}")  # "               Tomek"
print(f"{user:<30}")  # "Tomek                         "

print(liczba)  # 134632344532
print("Nasza duza liczba {:,}".format(liczba))  # Nasza duza liczba 134,632,344,532
print("Nasza duza liczba {:,}".format(liczba).replace(",", "."))  # Nasza duza liczba 134.632.344.532
print("Nasza duza liczba {:,}".format(liczba).replace(",", " "))  # Nasza duza liczba 134 632 344 532
