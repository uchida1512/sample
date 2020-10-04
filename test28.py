class Counter:
    def __init__(self, count, stepv, upper, lower, times):
        self.count = count  # 50
        self.stepv = stepv  # 15
        self.upper = upper  # 90
        self.lower = lower  # 6
        self.times = times  # 10

    def increment(self):
        if self.count > self.upper - self.stepv:
            pass
        elif self.count < self.lower - self.stepv:
            pass
        else:
            self.count += self.stepv

    def decrement(self):
        if self.count < self.lower + self.stepv:
            pass
        elif self.count > self.upper + self.stepv:
            pass
        else:
            self.count -= self.stepv

    def count_up(self):
        for i in range(self.times):
            self.increment()
        return self.count

    def count_down(self):
        for i in range(self.times):
            self.decrement()
        return self.count


x = Counter(50, 15, 90, 6, 10)

print(x.count_up())  # 80
print(x.count_down())  # 20