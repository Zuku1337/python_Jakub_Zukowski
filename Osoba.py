class Osoba:

    def __init__(self, imie: str, nazwisko: str):
        self._imie = imie
        self._nazwisko = nazwisko

    def __str__(self) -> str:
        return """To jest klasa Osoba:\n Imie:{} \n Nazwisko: {}""".format(self._imie, self._nazwisko)

    @property
    def imie(self) -> str:
        return self._imie

    @property
    def nazwisko(self) -> str:
        return self._nazwisko
