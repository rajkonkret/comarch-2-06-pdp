import sqlite3

# sqlite - baza sql w jednym pliku
try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    cursor = sql_connection.cursor()
    print("Baza zostałą podlączona....")
except sqlite3.Error as e:
    print("Błąd podczas połacenia z bazą", e)
finally:
    if sql_connection:
        sql_connection.close()
        print('Baza została zamknięta')

# Baza zostałą podlączona....
# Baza została zamknięta