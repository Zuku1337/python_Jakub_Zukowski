from Odcinek import Odcinek
from Pojazd import Pojazd

class Kurs:

    def __init__(self, cennik: float, odcinek: Odcinek, pojazd: Pojazd, czy_vip:bool, czy_premier: bool) -> None:
        self._cennik = cennik
        self._odcinek = odcinek
        self._pojazd = pojazd
        self._czy_vip = czy_vip
        self._czy_premier = czy_premier

    def __str__(self):
        return """Kurs:\nCennik: {}\nOdcinek: {}\nPojazd: {}\nCzy VIP: {}\nCzy premier: {}"""\
            .format(self._cennik, self._odcinek, self._pojazd, self._czy_vip, self._czy_premier)

    @property
    def cennik(self) -> float:
        return self._cennik

    @cennik.setter
    def cennik(self, value: float) -> None:
        self._cennik = value

    @property
    def suma(self) -> float:
        return self._suma

    @suma.setter
    def suma(self) -> None:
        self._suma = self.get_suma()

    @property
    def odcinek(self) -> Odcinek:
        return self._odcinek

    @odcinek.setter
    def odcinek(self, value: Odcinek) -> None:
        self._odcinek = value

    @property
    def pojazd(self) -> Pojazd:
        return self._pojazd

    @pojazd.setter
    def pojazd(self, value: Pojazd) -> None:
        self._pojazd = value

    @property
    def czy_vip(self) -> bool:
        return self._czy_vip

    @czy_vip.setter
    def czy_vip(self, value: bool) -> None:
        self._czy_vip = value

    def get_pojazd(self) -> Pojazd.marka:
        return self.pojazd.marka

    def get_suma(self) -> float:
        return self.odcinek.dlugosc * self.cennik
