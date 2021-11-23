class Library:

    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self) -> str:
        return f"Klasa biblioteka - obiekty:\n" \
               f"{self.city} - Miasto\n" \
               f"{self.street} - Ulica\n" \
               f"{self.zip_code} - Kod pocztowy\n" \
               f"{self.open_hours} - Godziny otwarcia\n" \
               f"{self.phone} - Numer telefonu\n"
