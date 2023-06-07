import sqlite3

# sqlite - baza sql w jednym pliku
try:
    sql_connection = sqlite3.connect('sqlite_python.db')

    query = '''
    CREATE TABLE SqliteDb_developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joining_date datetime,
    salary REAL NOT NULL);
    '''

    with open('tables.sql', 'r') as file:
        sql_script = file.read()

    cursor = sql_connection.cursor()
    print("Baza zostałą podlączona....")

    cursor.executescript(sql_script)

    # cursor.execute(query)
    # sql_connection.commit()
except sqlite3.Error as e:
    print("Błąd podczas połacenia z bazą", e)
finally:
    if sql_connection:
        sql_connection.close()
        print('Baza została zamknięta')
