import csv

filename = 'records.csv'

fields = []
rows = []

with open(filename, 'r') as csv_f:
    csvreader = csv.reader(csv_f)

    print(type(csvreader))  # <class '_csv.reader'>

    # next - zapisze pierwszy wiersz do fields
    # ustawi wskaznik na drugi element kolekcji
    fields = next(csvreader)

    # ta petla wystartuje nie od poczatku kolekcji a od indeksu 1, czyli od drugiego elementu
    for row in csvreader:
        rows.append(row)

print(fields)  # ['name', 'branch', 'year', 'cgpa']
print(rows)  # [['Radek', 'COE', '2', '9.1']]
print(rows[0])  # ['Radek', 'COE', '2', '9.1']

for p in zip(fields, rows[0]):
    print(p)

# ('name', 'Radek')
# ('branch', 'COE')
# ('year', '2')
# ('cgpa', '9.1')
