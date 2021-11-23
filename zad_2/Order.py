class Order:

    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self) -> str:
        return f"{self.employee} - Pracownik\n" \
               f"{self.student} - Student\n" \
               f"{self.books} - Książki\n" \
               f"{self.order_date} - Data wypożyczenia\n"
