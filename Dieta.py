from Dietetyk import Dietetyk


class Dieta:

    def __init__(self, nazwa: str, koszt: float, dietetyk: Dietetyk, kalorycznosc: int) -> None:
        self._nazwa = nazwa
        self._koszt = koszt
        self._dietetyk = dietetyk
        self._kalorycznosc = kalorycznosc

    def __str__(self) -> str:
        return """To jest klasa Dieta:\n Nazwa:{} \n Koszt: {} \n Polecający: {} \n Kalorycznosc: {}""" \
            .format(self._nazwa, self._koszt, self._dietetyk, self._kalorycznosc)

    @property
    def nazwa(self) -> str:
        return self._nazwa

    @property
    def koszt(self) -> float:
        return self._koszt

    @property
    def dietetyk(self) -> Dietetyk:
        return self._dietetyk

    @property
    def kalorycznosc(self) -> int:
        return self._kalorycznosc
