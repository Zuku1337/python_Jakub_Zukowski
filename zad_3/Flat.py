from Property import Property


class Flat(Property):

    def __init__(self, area, rooms: int, price, address, floor):
        self.floor = floor
        super().__init__(area, rooms, price, address)

    def __str__(self) -> str:
        return f"Klasa Mieszkanie - obiekty:\n" \
               f"{self.floor} - Piętro\n" \
               f"{self.area} - Metraż\n" \
               f"{self.rooms} - Pokoje\n" \
               f"{self.price} - Cena\n" \
               f"{self.address} - Adres"
