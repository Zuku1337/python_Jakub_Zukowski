from Odcinek import Odcinek
from Pojazd import Pojazd

class Kurs:

    def __init__(self) -> None:
        self._cennik = None
        self._odcinek = None
        self._suma = None
        self._pojazd = None
        self._czy_vip = None
        self._czy_premier = None

    def __str__(self):
        return """Kurs:\nCennik: {}\nSuma: {}\nOdcinek: {}\nPojazd: {}\nCzy VIP: {}"""\
            .format(self._cennik, self._suma, self._odcinek, self._pojazd, self._czy_vip)

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
    def pojazd(self) -> Pojazd.marka:
        return self._pojazd

    @pojazd.setter
    def pojazd(self) -> None:
        self._pojazd = self.get_pojazd()

    @property
    def czy_vip(self) -> bool:
        return self._czy_vip

    @czy_vip.setter
    def czy_vip(self, value: bool) -> None:
        self._czy_vip = value

    def get_pojazd(self) -> Pojazd.marka:
        return Pojazd.marka

    def get_suma(self) -> float:
        suma = 0
        if isinstance(self.odcinek, list):
            for i in self.odcinek.dlugosc:
                suma += i * self.cennik
        else:
            suma += self.odcinek * self.cennik
        return suma