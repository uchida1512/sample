import pytest


class ABC:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def sub(self) -> int:
        if self._x_or_y_is_not_int():
            raise ValueError('整数を入力してください')
        elif self._x_or_y_is_negative_number():
            raise ValueError('正数を入力してください')
        return self.x - self.y

    def _x_or_y_is_not_int(self) -> bool:
        return not isinstance(self.x or self.y, int)

    def _x_or_y_is_negative_number(self) -> bool:
        return (self.x or self.y) < 0


a = ABC(3, 4)
print(a.sub())
b = ABC(-5, 4)
print(b.sub())