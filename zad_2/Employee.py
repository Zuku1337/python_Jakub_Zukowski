class Employee:

    def __init__(self, first_name, last_name, hire_date, birth_date,city,street,zip_code,phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"To jest klasa pracownik zawierająca obiekty:\n" \
               f"{self.first_name} - Imie pracownika\n" \
               f"{self.last_name} - Nazwisko pracownika\n" \
               f"{self.hire_date} - Data zaczęcia pracy\n" \
               f"{self.birth_date} - Data urodzenia\n" \
               f"{self.city} - Miasto zamieszkania\n" \
               f"{self.street} - Ulica\n" \
               f"{self.zip_code} - Kod pocztowy\n" \
               f"{self.phone} - Numer telefonu\n"
