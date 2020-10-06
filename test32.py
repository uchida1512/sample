"""
数をカウントできるようなクラスを実装する
・数はカウントアップ（ダウン）するたびに、指定の刻み幅ずつ増える（減る）
・カウントの上限と下限、初期値及び刻み幅を指定できるようにする
・カウントをリセットできるようにする
"""
import pytest


class Counter:
    def __init__(self, value: int, step: int, upper_limit=90, lower_limit=0):
        self.value = value  # 50
        self.step = step  # 15
        self.upper_limit = upper_limit  # 90
        self.lower_limit = lower_limit  # 0

    def up(self) -> int:
        """指定された刻み幅分増やす"""
        if self.value <= self.upper_limit - self.step:
            self.value += self.step
            return self.value
        else:
            raise ValueError('CanNotCountUpError')

    def down(self) -> int:
        """指定された刻み幅分減らす"""
        if self.value >= self.lower_limit + self.step:
            self.value -= self.step
            return self.value
        else:
            raise ValueError('CanNotCountDownError')

    def reset(self) -> int:
        """カウントをリセットする"""
        self.value = 0
        return self.value


counter = Counter(value=50, step=15)

counter.up()
counter.up()
print(counter.value)  # 80

counter.down()
print(counter.value)  # 65

counter.reset()
print(counter.value)  # 0



def test_カウンターの初期値は指定できる():
    counter = Counter(value=7, step=1)

    assert counter.value == 7


def test_カウンターの刻み幅は指定できる():
    counter = Counter(value=0, step=3)

    counter.up()

    assert counter.value == 3


def test_カウントをリセットできる():
    counter = Counter(value=0, step=3)

    counter.up()
    counter.up()
    counter.up()

    counter.reset()

    assert counter.value == 0


def test_カウントダウンできる():
    counter = Counter(value=0, step=3)

    counter.up()
    counter.up()
    counter.down()

    assert counter.value == 3


def test_上限を超えるようなカウントアップはできない():
    counter = Counter(value=100, step=1, upper_limit=100)

    with pytest.raises(ValueError):
        counter.up()


def test_0を下回るようなカウントダウンはできない():
    counter = Counter(value=0, step=1, lower_limit=0)

    with pytest.raises(ValueError):
        counter.down()