from Property import Property


class House(Property):

    def __init__(self, area, rooms: int, price, address, plot: int):
        self.plot = plot
        super().__init__(area, rooms, price, address)

    def __str__(self) -> str:
        return f"Klasa Mieszkanie - obiekty:\n" \
               f"{self.plot} - Rozmiar działki\n" \
               f"{self.area} - Metraż\n" \
               f"{self.rooms} - Pokoje\n" \
               f"{self.price} - Cena\n" \
               f"{self.address} - Adres"
