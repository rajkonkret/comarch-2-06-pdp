import sqlite3

# sqlite - baza sql w jednym pliku
try:
    sql_connection = sqlite3.connect('sqlite_python.db')

    insert = '''
    INSERT INTO software (id,name,price) VALUES(1,'Python', 200);
    '''
    cursor = sql_connection.cursor()
    print("Baza zostałą podlączona....")

    cursor.execute(insert)
    sql_connection.commit()
except sqlite3.Error as e:
    print("Błąd podczas połacenia z bazą", e)
finally:
    if sql_connection:
        sql_connection.close()
        print('Baza została zamknięta')

# Baza zostałą podlączona....
# Baza została zamknięta
