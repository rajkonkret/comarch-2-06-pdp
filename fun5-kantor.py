def kantor(waluta):
    print("Uruchomienie kantoru")

    def usd(kwota=0):
        print("Przeliczam dolary", kwota * 4.13, "zł")

    def eur(kwota=0):
        print("Przeliczam euro", kwota * 4.50, "zł")

    if waluta == 'eur':
        return eur
    else:
        return usd


moj_kantor_eur = kantor('eur')
print(moj_kantor_eur)  # <function kantor.<locals>.eur at 0x10310c7c0>
moj_kantor_eur()  # Przeliczam euro
moj_kantor_eur(1000)  # Przeliczam euro 4500.0 zł

moj_kantor_usd = kantor("usd")
moj_kantor_usd(5000)  # Przeliczam dolary 20650.0 zł
