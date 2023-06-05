odp = True
print(odp)
print(type(odp))  # <class 'bool'>

if odp:
    print("Brawo")  # wciecie obowiazkowe 4 spacje
else:
    print("Musisz sie uczyc")

print("Program działa nadal")

# 15:00
# podatek = 0.0
#
# zarobki = int(input('Podaj dochód'))
# if zarobki < 10000:
#     podatek = 0.0
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.6
#
# print(f"Zapłacisz  {zarobki * podatek} zł")
# # dla dochodow od 10000 do 30000 podatek 0.2

suma_zam = 150
if suma_zam > 100:
    rabacik = 25
else:
    rabacik = 0

print(f"Rabacik {rabacik}")  # Rabacik 25

rabat = 25 if suma_zam > 100 else 0
print(f"Rabacik {rabat}")  # Rabacik 25

lista_bledow = []
alert_system = 'email'
error = 'critical'
error_message = "Stało się coś strasznego"

if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    if error == 'medium':
        lista_bledow.append("ostrzeżenie")
    elif error == 'critical':
        lista_bledow.append('krytyczny')
    else:
        lista_bledow.append('nieznany')

print(lista_bledow)
# Zrobic test z historii
# wyswietlic pytanie
# pobrac odpowiedz
# sprawdzic czy prawidłowa i wyswietlic odpowiedni komunikat
print("Podaj date Chrztu Polski")
odp = input("Podaj odpowiedź")
if odp == '966':
    print("odpowiedź prawidłowa")
else:
    print("Masz w podręczniku na stronie 23")