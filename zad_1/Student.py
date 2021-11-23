class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Klasa student - obiekty:\n" \
               f"{self.name} - Imię studenta\n" \
               f"{self.marks} - Oceny studenta"

    def is_passed(self) -> bool:
        if self.marks > 50:
            return True
        return False
