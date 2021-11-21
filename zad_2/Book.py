class Book:

    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"To jest klasa książka zawierająca obiekty:\n" \
               f"{self.library} - Biblioteka\n" \
               f"{self.publication_date} - Data publikacji\n" \
               f"{self.author_name} - Imie autora\n" \
               f"{self.author_surname} - Nazwisko autora\n" \
               f"{self.number_of_pages} - Ilość stron\n"