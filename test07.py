import math


class Square:
    def __init__(self, wide):
        self.wide = wide

    def diagonal(self):
        return math.sqrt(self.wide ** 2 + self.wide ** 2)


s = Square(2)
print(s.diagonal())

print(math.sqrt(2) * 2)
print(math.sqrt(2) * 4)