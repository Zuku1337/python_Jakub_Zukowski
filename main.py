from Firma import FirmaTransportowa, FirmaSpozywcza
from Pojazd import Pojazd

if __name__ == '__main__':
    firm1 = FirmaTransportowa("Test1", "Kowalski Piotr", "Szypiorkowa 21/37", 2137.38, "Kurier", "Volvo")
    firm2 = FirmaSpozywcza("Test2", "Nowak Paweł", "Tucznikowa 123", 455.66, "Spożywka", "Biedronka")
    pojazd1 = Pojazd("volkswagen", "Passat", 4, 500, False)
    print(firm1)
    print(firm2)
    print(pojazd1)