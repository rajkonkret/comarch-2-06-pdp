# kalkulator
# menu
# wybor dziłania
# pobranie liczb od użytkownika
# wyswietlenie dziłąnia
# obsłuzymy wyjątki jakie sie pojawia podczas działania kalkulatora

while True:
    print("""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec""")

    odp = input("Podaj działąnie jakie chcesz wykonać")
    if odp == '5':
        break
    try:
        a = int(input("Podaj pierwszą liczbę"))
        b = int(input("Podaj drugą liczbę"))

        if odp == '1':
            print(f"Wynik działania {a} + {b} = {a + b}")
            # wynik działania a  + b  = wynik
        elif odp == '2':
            print(f"Wynik działania {a} - {b} = {a - b}")
        elif odp == '3':
            print(f"Wynik działania {a} * {b} = {a * b}")
        elif odp == '4':
            print(f"Wynik działania {a} / {b} = {a / b}")
        else:
            print(f"Nie znam takiego działania")
    except ZeroDivisionError:
        print("Nie dziel przez zero")  # Nie dziel przez zero
    except ValueError:
        print("Bład wartosci")
    except TypeError:
        print("Błąd typu")
    except Exception as e:
        print("Bład ", e)
    else:
        print("Gdy nie ma błedu")
    finally:
        print("Zawsze")
