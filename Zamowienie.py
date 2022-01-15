from Osoba import Osoba
from Dieta import Dieta
from Pacjent import Pacjent


class Zamowienie():

    def __init__(self, dieta: list, kierowca: Osoba, miejsce_dostarczenia: str, odbiorca: Pacjent) -> None:
        self._dieta = dieta
        self._kierowca = kierowca
        self._miejsce_dostarczenia = miejsce_dostarczenia
        self._odbiorca = odbiorca

    def __str__(self) -> str:

        return """To jest klasa Zamowienie:\n Dieta:{} \n Kierowca: {} {} \n Miejsce dostarczenia: {} \n Odbiorca: {} {}""".format(
            self.diets(), self._kierowca.imie, self._kierowca.nazwisko, self._odbiorca.miejsce_zamieszkania, self._odbiorca.imie, self._odbiorca.nazwisko)

    @property
    def dieta(self) -> list:
        return self._dieta

    @dieta.setter
    def dieta(self, value: list) -> None:
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
    def miejsce_dostarczenia(self, value: str) -> None:
        self._miejsce_dostarczenia = value

    @property
    def odbiorca(self) -> Pacjent:
        return self._odbiorca

    @odbiorca.setter
    def odbiorca(self, value: Pacjent) -> None:
        self._odbiorca = value

    def value_calc(self) -> float:
        value = 0
        for i in self.dieta:
            value += i.koszt
        return round(value, 2)

    def kal_calc(self) -> int:
        value = 0
        for i in self.dieta:
            value += i.kalorycznosc
        return value

    def diets(self):
        nazwy_scal = ""
        for i in self.dieta:
            nazwy_scal += " " + i.nazwa
        return nazwy_scal