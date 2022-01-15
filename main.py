from Zamowienie import Zamowienie
from Dieta import Dieta
from Dietetyk import Dietetyk
from Osoba import Osoba
from Pacjent import Pacjent

if __name__ == "__main__":
    Kierowca = Osoba("Janusz", "Kowalski")
    Dietetyk = Dietetyk("Janusz", "Ziemba", 50, "Watykan")
    Dieta_1 = Dieta("Wariant_1", 21.37, Dietetyk, 2137)
    Dieta_2 = Dieta("Wariant_2", 21.37, Dietetyk, 2137)
    Pacjent = Pacjent("Jakub", "Żukowski", "1970-01-01", "Sosnowiec (niestety)")
    zam_1 = Zamowienie(list([Dieta_1, Dieta_2]), Kierowca, "Szczypiorkowa 21/37", Pacjent)
    print(zam_1)
    print("Zamówienie ma tyle kalorii %s" % zam_1.kal_calc())
    print("Zamówienie tyle kosztuje %s" % zam_1.value_calc())