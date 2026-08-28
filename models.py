class Person:
    def __init__(self, name, age, member_id):
        self._name = name
        self._age = age
        self._member_id = member_id

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def member_id(self):
        return self._member_id

    def __str__(self):
     return f"{self.name} (ID: {self.member_id})"


class Member(Person):
    def __init__(self, name, age, member_id, membership_type):
        super().__init__(name, age, member_id)
        self._membership_type = membership_type
        self._borrowed_books = []

    @property
    def membership_type(self):
        return self._membership_type

    @property
    def borrowed_books(self):
        return self._borrowed_books

    def describe(self):
        return (
            f"Member: {self.name}, "
            f"ID: {self.member_id}, "
            f"Membership: {self.membership_type}, "
            f"Borrowed books: {self.borrowed_books}"
        )

class Librarian(Person):
    def __init__(self, name, age, member_id, employee_id):
        super().__init__(name, age, member_id)
        self._employee_id = employee_id

    @property
    def employee_id(self):
        return self._employee_id

    def describe(self):
        return (
            f"Librarian: {self.name}, "
            f"ID: {self.member_id}, "
            f"Employee ID: {self.employee_id}"
        )   