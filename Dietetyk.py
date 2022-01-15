from Osoba import Osoba


class Dietetyk(Osoba):

    def __init__(self, imie: str, nazwisko: str, doswiadczenie: int, miejsce_pracy: str) -> None:
        self._doswiadczenie = doswiadczenie
        self._miejsce_pracy = miejsce_pracy
        super().__init__(imie, nazwisko)

    def __str__(self) -> str:
        return """To jest klasa Dietetyk:\n Imie:{} \n Nazwisko: {} \n Doswiadczenie: {} \n Miejsce pracy: {}""" \
            .format(self._imie, self._nazwisko, self._doswiadczenie, self._miejsce_pracy)

    @property
    def doswiadczenie(self) -> int:
        return self._doswiadczenie

    @property
    def miejsce_pracy(self) -> str:
        return self._miejsce_pracy
