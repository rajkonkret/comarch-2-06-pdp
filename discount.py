from datetime import date, timedelta, datetime

today = date.today()
time = datetime.now()

print(today)  # 2023-06-06
print(time)  # 2023-06-06 10:31:57.880648

print(type(today))  # <class 'datetime.date'>

# days = 0, seconds = 0, microseconds = 0,
# milliseconds = 0, minutes = 0, hours = 0, weeks = 0
tommorow = today + timedelta(days=1)
print(tommorow)  # 2023-06-07

print(time.hour)
print(today.day)

products = [
    {'sku': '1', "exp_date": today, 'price': 100.0},
    {'sku': '2', "exp_date": tommorow, 'price': 50},
    {'sku': '3', "exp_date": today, 'price': 20.0},
    {'sku': '4', "exp_date": today, 'price': 70},
    {'sku': '5', "exp_date": today, 'price': 220.0},
    {'sku': '6', "exp_date": tommorow, 'price': 120.0},
]

print(products)

for product in products:
    if product['exp_date'] != today:
        continue  # wróci na poczatek pętli i zacznie wykonywnaie dla kolejnego elementu
    print(product)
    product['price'] *= 0.8  # p = p * 0.8

    print(f"""
    Price for sku= {product['sku']}
    is now {product['price']}""")
