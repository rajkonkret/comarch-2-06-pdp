# json  - {"name":"Radek"}
import json

person_dict = {'name': 'Radek', "age": 40, "czy_pali": None}
print(person_dict)  # {'name': 'Radek', 'age': 40, 'czy_pali': None}

with open('dane_nasze.json', 'w') as f:
    json.dump(person_dict, f)
# {"name": "Radek", "age": 40, "czy_pali": null}

with open('dane_nasze.json', 'r') as fh:
    data = json.load(fh)

print(data)
# {'name': 'Radek', 'age': 40, 'czy_pali': None}

print(data['name'])
print(data.keys())
print(data.values())
print(data.items())
# dict_keys(['name', 'age', 'czy_pali'])
# dict_values(['Radek', 40, None])
# dict_items([('name', 'Radek'), ('age', 40), ('czy_pali', None)])
