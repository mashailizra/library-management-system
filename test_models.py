from models import Member


member1 = Member("Anu", 25, "M001", "Premium")
member2 = Member("Meera", 22, "M002", "Basic")


print("=== __str__ Test ===")
print(member1)
print(member2)


print("\n=== __repr__ Test ===")
print(repr(member1))
print(repr(member2))


print("\n=== List Test ===")
members = [member1, member2]
print(members)