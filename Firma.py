class Firma:

    def __init__(self, nazwa: str, szef: str, adres: str, kapital: float, uslugi: str) -> None:
        self._nazwa = nazwa
        self._szef = szef
        self._adres = adres
        self._kapital = kapital
        self._uslugi = uslugi

    def __str__(self) -> str:
        return """\nFirma:\nNazwa:{}\nSzef:{}\nAdres:{}\nKapital:{}\nUslugi:{}""" \
            .format(self._nazwa, self._szef, self._adres, self._kapital, self._uslugi)

    @property
    def nazwa(self) -> str:
        return self._nazwa

    @nazwa.setter
    def nazwa(self, value: str) -> None:
        self._nazwa = value

    @property
    def szef(self) -> str:
        return self.szef

    @szef.setter
    def szef(self, value: str) -> None:
        self._szef = value

    @property
    def adres(self) -> str:
        return self._adres

    @adres.setter
    def adres(self, value: str) -> None:
        self._adres = value

    @property
    def kapital(self) -> float:
        return self._kapital

    @kapital.setter
    def kapital(self, value: float) -> None:
        self._kapital = value

    @property
    def uslugi(self) -> str:
        return self._uslugi

    @uslugi.setter
    def uslugi(self, value: str) -> None:
        self._uslugi = value


class FirmaTransportowa(Firma):

    def __init__(self, nazwa: str, szef: str, adres: str, kapital: float, uslugi: str, marka_aut: str) -> None:
        self._marka_aut = marka_aut
        super().__init__(nazwa, szef, adres, kapital, uslugi)

    def __str__(self) -> str:
        prefix = super().__str__()
        return """{}\nMarka aut:{}\n""".format(prefix, self._marka_aut)

    @property
    def marka_aut(self) -> str:
        return self._marka_aut

    @marka_aut.setter
    def marka_aut(self, value: str) -> None:
        self._marka_aut = value


class FirmaSpozywcza(Firma):

    def __init__(self, nazwa: str, szef: str, adres: str, kapital: float, uslugi: str, siec_sklepow: str) -> None:
        self._siec_sklepow = siec_sklepow
        super().__init__(nazwa, szef, adres, kapital, uslugi)

    def __str__(self) -> str:
        prefix = super().__str__()
        return """{}\nSiec sklepow:{}\n""".format(prefix, self._siec_sklepow)

    @property
    def siec_sklepow(self) -> str:
        return self._siec_sklepow

    @siec_sklepow.setter
    def siec_sklepow(self, value: str) -> None:
        self._siec_sklepow = value