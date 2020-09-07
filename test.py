class Person:
    def __init__(self):
        self.name = 'Bob'


bob = Person()
another_bob = Person()

print(bob.name)  # 01
print(another_bob.name)  # 02

print(bob)  # 03
print(another_bob)  # 04

same_bob = bob
same_bob02 = same_bob
print(bob is same_bob02)
print(same_bob)
# x = 5
# print(id(x))
# print(hex(id(x)))
# print(id(bob))
# print(hex(id(bob)))