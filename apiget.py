import requests as re

url = 'http://api.nbp.pl/api/exchangerates/rates/A/USD/'

response = re.get(url)
print(response)
# <Response [200]> - ok
# 4.. błedy zapytania, błedny adres
# 5.. bład serwera
table = response.json()
print(table)
# {'table': 'A', 'currency': 'dolar amerykański', 'code': 'USD',
#  'rates': [{'no': '108/A/NBP/2023', 'effectiveDate': '2023-06-06', 'mid': 4.1964}]}
print(table['rates'])  # [{'no': '108/A/NBP/2023', 'effectiveDate': '2023-06-06', 'mid': 4.1964}]
print(table['rates'][0])  # {'no': '108/A/NBP/2023', 'effectiveDate': '2023-06-06', 'mid': 4.1964}
print(table['rates'][0]['mid'])  # 4.1964
