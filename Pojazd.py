class Pojazd:

    def __init__(self, nazwa: str, marka: str, ilosc_osob: int, liczba_koni: int, kierownica_po_prawej: bool) -> None:
        self._nazwa = nazwa
        self._marka = marka
        self._ilosc_osob = ilosc_osob
        self._liczba_koni = liczba_koni
        self._kierownica_po_prawej = kierownica_po_prawej

    def __str__(self) -> str:
        return """Pojazd:\nNazwa: {}\nMarka: {}\nIlosc osob: {}\nLiczba koni: {}\nKierownica z prawej strony: {}\n"""\
            .format(self._nazwa, self._marka, self._ilosc_osob, self._liczba_koni, self._kierownica_po_prawej)

    @property
    def nazwa(self) -> str:
        return self._nazwa

    @nazwa.setter
    def nazwa(self, value: str) -> None:
        self._nazwa = value

    @property
    def marka(self) -> str:
        return self._marka

    @marka.setter
    def marka(self, value: str) -> None:
        self._marka = value

    @property
    def ilosc_osob(self) -> int:
        return self.ilosc_osob

    @ilosc_osob.setter
    def ilosc_osob(self, value: int) -> None:
        self._ilosc_osob = value

    @property
    def liczba_koni(self) -> int:
        return self._liczba_koni

    @liczba_koni.setter
    def liczba_koni(self, value: int) -> None:
        self._liczba_koni = value

    @property
    def kierownica_po_prawej(self) -> bool:
        return self._kierownica_po_prawej

    @kierownica_po_prawej.setter
    def kierownica_po_prawej(self, value: bool) -> None:
        self._kierownica_po_prawej = value
