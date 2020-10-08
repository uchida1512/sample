import pytest


class CanNotCountDownError(ValueError):
    pass


class CanNotCountUpError(ValueError):
    pass


class Counter:
    def __init__(self,
                 value: int, step: int,
                 upper_limit: int = 100,
                 lower_limit: int = 0):
        self.step = step
        self.value = value
        self.upper_limit = upper_limit
        self.lower_limit = lower_limit

    def up(self) -> None:
        if self._will_go_over_upper_limit():
            raise CanNotCountUpError('カウント上限を上回るカウントアップはできません')

        self.value += self.step

    def down(self) -> None:
        if self._will_be_below_lower_limit():
            raise CanNotCountDownError('カウント下限を下回るカウントダウンはできません')

        self.value -= self.step

    def reset(self) -> None:
        self.value = 0

    def _will_be_below_lower_limit(self) -> bool:
        return self.value - self.step < self.lower_limit

    def _will_go_over_upper_limit(self) -> bool:
        return self.value + self.step > self.upper_limit


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

    with pytest.raises(CanNotCountUpError):
        counter.up()


def test_0を下回るようなカウントダウンはできない():
    counter = Counter(value=0, step=1)

    with pytest.raises(CanNotCountDownError):
        counter.down()