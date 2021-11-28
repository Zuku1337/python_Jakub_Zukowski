from Firma import FirmaTransportowa, FirmaSpozywcza
from Pojazd import Pojazd
from Odcinek import Odcinek
from Kurs import Kurs

if __name__ == '__main__':
    firm1 = FirmaTransportowa("Test1", "Kowalski Piotr", "Szypiorkowa 21/37", 2137.38, "Kurier", "Volvo")
    firm2 = FirmaSpozywcza("Test2", "Nowak Paweł", "Tucznikowa 123", 455.66, "Spożywka", "Biedronka")
    pojazd1 = Pojazd("volkswagen", "Passat", 4, 500, False)
    odc1 = Odcinek(23.1, "Bytom-Kraków", firm1, False, True)
    odc2 = Odcinek(23.1, "Bytom-Kraków", firm1, False, True)
    kurs1 = Kurs()
    kurs1.odcinek = odc1
    kurs1.cennik = 2.5
    kurs1.pojazd = pojazd1
    kurs1.czy_vip = True
    kurs1.suma = kurs1.get_suma()
    print(firm1)
    print(firm2)
    print(pojazd1)
    print(odc1)
    print(kurs1)