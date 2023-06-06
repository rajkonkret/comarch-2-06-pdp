class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    raise MyException("Wystąpił błąd")
except MyException:
    print("Wystapił wyjątek MyException")
except Exception as e:
    print(e)
