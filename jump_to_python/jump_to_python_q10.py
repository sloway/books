class Calculator:
    def __init__(self, inputs):
        self.inputs = inputs

    def sum(self):
        total = 0
        for v in self.inputs:
            total += v
        return total

    def avg(self):
        return self.sum() / len(self.inputs)


cal1 = Calculator([1, 2, 3, 4, 5])
print(cal1.sum())
print(cal1.avg())

cal2 = Calculator([6, 7, 8, 9, 10])
print(cal2.sum())
print(cal2.avg())
