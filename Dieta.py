from Dietetyk import Dietetyk

class Dieta:

    def __init__(self, nazwa:str, koszt:float, dietetyk: Dietetyk, czy_gluten: bool) -> None:
        self._nazwa = nazwa
        self._koszt = koszt
        self._dietetyk = dietetyk
        self._czy_gluten = czy_gluten

    def __str__(self) -> str:
        """To jest klasa Dieta:\n Nazwa:{} \n Koszt: {} \n Polecający: {} \n Czy gluten: {}"""\
            .format(self._nazwa, self._koszt, self._polecajacy, self._czy_gluten)

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
    def czy_gluten(self) -> bool:
        return self._czy_gluten

