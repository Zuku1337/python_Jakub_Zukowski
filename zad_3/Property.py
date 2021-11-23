class Property:

    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self) -> str:
        return f"Klasa Nieruchomość - obiekty:\n" \
               f"{self.area} - Metraż\n" \
               f"{self.rooms} - Pokoje\n" \
               f"{self.price} - Cena\n" \
               f"{self.address} - Adres"
