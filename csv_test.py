import csv

# pliki csv - dane oddzielone sa znakiem podziału (, ; spacja tab)
# Radek,Marek,Zenek

fields = ['name', 'branch', 'year', 'cgpa']
# ['radek', 'COE', '3', '9.1']
my_list_dict = [
    {'branch': "COE", 'cgpa': '9.1', "year": 2, 'name': 'Radek'},
]

filename = 'records.csv'

with open(filename, 'w', newline='') as csv_f:
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerows(my_list_dict)
