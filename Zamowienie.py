from Osoba import Osoba
from Dieta import Dieta
from Pacjent import Pacjent


class Zamowienie():

    def __init__(self, dieta: list(Dieta), kierowca: Osoba, miejsce_dostarczenia: str, odbiorca: str) -> None:
        self._dieta = dieta
        self._kierowca = kierowca
        self._miejsce_dostarczenia = miejsce_dostarczenia
        self._odbiorca = odbiorca

    def __str__(self) -> None:
        """To jest klasa Zamowienie:\n Dieta:{} \n Kierowca: {} \n Miejsce dostarczenia {} \n Odbiorca""".format(self._imie, self._nazwisko, self._miejsce_dostarczenia, self._odbiorca)

    @property
    def dieta(self) -> list(Dieta):
        return  self._dieta

    @dieta.setter
    def dieta(self, value: list(Dieta)) -> None:
        self._dieta = value

    @property
    def kierowca(self) -> Osoba:
        return self._dieta

    @kierowca.setter
    def kierowca(self, value: Osoba) -> None:
        self._kierowca = value

    @property
    def miejsce_dostarczenia(self) -> str:
        return self._miejsce_dostarczenia

    @miejsce_dostarczenia.setter
    def miejsce_dostarczenia(self, value:str) -> None:
        self._miejsce_dostarczenia = value

    @property
    def odbiorca(self) -> str:
        return self._odbiorca

    @odbiorca.setter
    def odbiorca(self, value:str) -> None:
        self._odbiorca = value