def dekor(funk):
    def wew():
        print("Dekorujemy")
        return funk()

    return wew


@dekor  # dekorujemy funkcje hej() za pomoca funkcji dekor()
def hej():
    print("Hej")


hej()
