import json 

class DuplicateMemberError(Exception):
    pass


class MemberNotFoundError(Exception):
    pass



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

    @borrowed_books.setter
    def borrowed_books(self, books):
        self._borrowed_books = books

    def describe(self):
        return (
            f"Member: {self.name}, "
            f"ID: {self.member_id}, "
            f"Membership: {self.membership_type}, "
            f"Borrowed books: {self.borrowed_books}"
        )
    def __str__(self):
        return f"{self.name} (Member ID: {self.member_id})"

    def __repr__(self):
        return (
            f"Member(name='{self.name}', "
            f"age={self.age}, "
            f"member_id='{self.member_id}', "
            f"membership_type='{self.membership_type}')"
        )
    def __eq__(self, other):
        if not isinstance(other, Member):
            return NotImplemented

        return self.member_id == other.member_id
    
    def __lt__(self, other):
        if not isinstance(other, Member):
            return NotImplemented

        return self.name < other.name

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "member_id": self.member_id,
            "membership_type": self.membership_type,
            "borrowed_books": self.borrowed_books.copy(),
        }

    @classmethod
    def from_dict(cls, data):
        member = cls(
            data["name"],
            data["age"],
            data["member_id"],
            data["membership_type"],
        )

        member._borrowed_books = data["borrowed_books"].copy()

        return member
    
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
class Library:
    def __init__(self, members=None):
        self.members = members if members is not None else []

    def __add__(self, other):
        if not isinstance(other, Library):
            return NotImplemented

        return Library(self.members + other.members)
    
    def add_member(self, member):
        for existing_member in self.members:
            if existing_member.member_id == member.member_id:
                raise DuplicateMemberError(
                    f"Member with ID {member.member_id} already exists."
                )

        self.members.append(member)

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member

        raise MemberNotFoundError(
            f"Member with ID {member_id} was not found."
        )    
    def save_to_json(self, filename):
            data = [member.to_dict() for member in self.members]

            with open(filename, "w") as file:
                json.dump(data, file, indent=4)

    @classmethod
    def load_from_json(cls, filename):
        with open(filename, "r") as file:
            data = json.load(file)

        members = [Member.from_dict(item) for item in data]

        return cls(members)