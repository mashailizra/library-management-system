from models import Member, Librarian


member1 = Member("Anu", 25, "M001", "Premium")
member2 = Member("Meera", 22, "M002", "Basic")

librarian = Librarian("Rahul", 32, "L001", "EMP101")

member1.borrowed_books.append("Python Crash Course")
member1.borrowed_books.append("Clean Code")

member2.borrowed_books.append("The Pragmatic Programmer")


people = [member1, member2, librarian]


print("=== Polymorphism Test ===")

for person in people:
    print(person.describe())


print("\n=== __str__ Test ===")

for person in people:
    print(person)