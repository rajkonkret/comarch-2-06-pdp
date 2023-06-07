import sqlite3

# sqlite - baza sql w jednym pliku
try:
    sql_connection = sqlite3.connect('sqlite_python.db')

    select = '''
    SELECT * FROM software;
    '''

    delete = '''
    DELETE FROM software where id = 1;
    '''
    update = '''
    UPDATE software SET price = 2000 WHERE id = 1;
    '''
    cursor = sql_connection.cursor()
    print("Baza zostałą podlączona....")  # (1, 'Python', 200.0)

    for row in cursor.execute(select):
        print(row)

    cursor.execute(update)  # (1, 'Python', 2000.0)
    sql_connection.commit()

except sqlite3.Error as e:
    print("Błąd podczas połacenia z bazą", e)
finally:
    if sql_connection:
        sql_connection.close()
        print('Baza została zamknięta')

# Baza zostałą podlączona....
# Baza została zamknięta
