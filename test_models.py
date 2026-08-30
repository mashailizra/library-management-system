from models import (
    Member,
    Library,
    DuplicateMemberError,
    MemberNotFoundError,
)


member1 = Member("Rahul", 25, "M001", "Premium")
member2 = Member("Anu", 22, "M002", "Basic")
member3 = Member("Meera", 28, "M003", "Premium")


member1.borrowed_books.append("Clean Code")
member2.borrowed_books.append("Python Crash Course")


print("=== 1. __str__ and __repr__ ===")
print(member1)
print(repr(member1))


print("\n=== 2. Equality Test ===")

same_member = Member("Another Rahul", 30, "M001", "Basic")

print("member1 == same_member:", member1 == same_member)


print("\n=== 3. Sorting Test ===")

members = [member1, member2, member3]

sorted_members = sorted(members)

for member in sorted_members:
    print(member)


print("\n=== 4. Library + Library ===")

library_a = Library([member1, member2])
library_b = Library([member3])

library_c = library_a + library_b

print("Library A:", library_a.members)
print("Library B:", library_b.members)
print("Combined Library:", library_c.members)


print("\n=== 5. Duplicate Member Test ===")

try:
    duplicate = Member("Duplicate", 30, "M001", "Basic")
    library_a.add_member(duplicate)
except DuplicateMemberError as error:
    print(error)


print("\n=== 6. Find Member Test ===")

try:
    found_member = library_a.find_member("M002")
    print("Found:", found_member)
except MemberNotFoundError as error:
    print(error)


print("\n=== 7. Member Not Found Test ===")

try:
    library_a.find_member("M999")
except MemberNotFoundError as error:
    print(error)


print("\n=== 8. JSON Save/Load Test ===")

library_a.save_to_json("members.json")

loaded_library = Library.load_from_json("members.json")

for member in loaded_library.members:
    print(member.describe())