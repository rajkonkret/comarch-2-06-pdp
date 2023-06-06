# argumenty slownikowe
def connect(**opcje):
    print(opcje)
    print(type(opcje))  # <class 'dict'>
    connect_param = {
        'host': '127.0.0.7',
        'port': '8080'
    }
    print(connect_param)  # {'host': '127.0.0.7', 'port': '8080'}
    connect_param['pwd'] = opcje
    print(connect_param)
    pwd = connect_param['pwd']
    print(type(pwd))  # <class 'dict'>
    # print(pwd['klucz'])

    connect_param.update({'pwd2': opcje})
    print(connect_param)


# TypeError: connect() takes 0 positional arguments but 5 were given
#
# connect(1, 2, 3, 4, 5)

connect(klucz='wartosc')  # {'klucz': 'wartosc'}
connect(a=7, b=9, c=0)
connect(radek="Test", host="/")
