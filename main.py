from Firma import FirmaTransportowa, FirmaSpozywcza
from Pojazd import Pojazd
from Odcinek import Odcinek
from Kurs import Kurs

if __name__ == '__main__':
    firm1 = FirmaTransportowa("Test1", "Kowalski Piotr", "Szypiorkowa 21/37", 2137.38, "Kurier", "Volvo")
    firm2 = FirmaSpozywcza("Test2", "Nowak Paweł", "Tucznikowa 123", 455.66, "Spożywka", "Biedronka")
    pojazd1 = Pojazd("volkswagen", "Passat", 4, 500, False)
    odc1 = Odcinek(23.1, "Bytom-Kraków", firm1, False, True)
    kurs1 = Kurs(2.5, odc1, pojazd1, True, False)
    print(firm1)
    print(firm2)
    print(pojazd1)
    print(odc1)
    print(kurs1)

    print(f"\nMarka pojazdu to: {kurs1.get_pojazd()}")
    print(f"Suma za kurs to: {kurs1.get_suma()}")