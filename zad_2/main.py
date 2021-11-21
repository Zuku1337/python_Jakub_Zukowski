from zad_1.Student import Student
from Book import Book
from Employee import Employee
from Library import Library
from Order import Order

student_1 = Student("Jakub", 55)
student_2 = Student("Patryk", 45)
library_1 = Library("Bytom", "Bytomska", "21/37", "21-37", 123456789)
library_2 = Library("Gdańsk", "Szczypiorkowa", "37/21", "37-21", 987654321)
book_1 = Book(library_1, 2001, "Patryk", "Tracz", 2137)
book_2 = Book(library_1, 2002, "Jakub", "Paweł", 1234)
book_3 = Book(library_2, 2003, "Paweł", "Tumulski", 927)
book_4 = Book(library_2, 2004, "Kasia", "Rower", 12352)
book_5 = Book(library_2, 20005, "ZYX", "XYZ", 6666)
employee_1 = Employee("Fiołek", "Los", "2021-01-01", "1999-03-22", "Bytom", "Bytomska", "21-37", 123456788)
employee_2 = Employee("Ariel", "Los", "2021-01-01", "1999-09-09", "Bytom", "Bytomska", "21-37", 123456777)
employee_3 = Employee("Doge", "Los", "2021-01-01", "1998-02-01", "Bytom", "Bytomska", "21-37", 1234567777)
order1 = Order(employee_2, student_1, [book_3, book_1], "2021-11-21")
order2 = Order(employee_1, student_2, book_5, "2021-11-21")
print(order1)
print(order2)

