from Firma import FirmaTransportowa

class Odcinek:

    def __init__(self, dlugosc: float, nazwa: str, firma: FirmaTransportowa, roboty_drogowe: bool, czy_czesto_stoi_policja: bool) -> None:
        self._dlugosc = dlugosc
        self._nazwa = nazwa
        self._firma = firma
        self._roboty_drogowe = roboty_drogowe
        self._czy_czesto_stoi_polica = czy_czesto_stoi_policja

    def __str__(self) -> str:
        return """Odcinek:\nDlugosc: {}\nNazwa: {}\n{}Roboty drogowe: {}\nCzy czesto stoi policja: {}"""\
            .format(self._dlugosc, self._nazwa, self._firma, self._roboty_drogowe, self._czy_czesto_stoi_polica)

    @property
    def dlugosc(self) -> float:
        return self._dlugosc

    @dlugosc.setter
    def dlugosc(self, value: float) -> None:
        self._dlugosc = value

    @property
    def nazwa(self) -> str:
        return self._nazwa

    @nazwa.setter
    def nazwa(self, value: str) -> None:
        self._nazwa = value

    @property
    def firma(self) -> FirmaTransportowa:
        return self._firma

    @firma.setter
    def firma(self, value: str) -> None:
        self._firma = value

    @property
    def roboty_drogowe(self) -> bool:
        return self._roboty_drogowe

    @roboty_drogowe.setter
    def roboty_drogowe(self, value: bool) -> None:
        self._roboty_drogowe = value

    @property
    def czy_czesto_stoi_policja(self) -> bool:
        return self._czy_czesto_stoi_polica

    @czy_czesto_stoi_policja.setter
    def czy_czesto_stoi_policja(self, value: bool) -> None:
        self._czy_czesto_stoi_polica = value


