from Osoba import Osoba

class Pacjent(Osoba):

    def __init__(self, imie:str,nazwisko:str,data_urodzenia:str, miejsce_zamieszkania:str) -> None:
        self._data_urodzenia = data_urodzenia
        self._miejsce_zamieszkania = miejsce_zamieszkania
        super().__init__(imie, nazwisko)

    def __str__(self) -> str:
        """To jest klasa Pacjent:\n Imie:{} \n Nazwisko: {} \n Data Urodzenia: {} \n Miejsce zamieszkania: {}"""\
            .format(self._imie, self._nazwisko, self._data_urodzenia, self._miejsce_zamieszkania)

    @property
    def data_urodzenia(self) -> str:
        return self._data_urodzenia

    @property
    def miejsce_zamieszkania(self) -> str:
        return self._miejsce_zamieszkania