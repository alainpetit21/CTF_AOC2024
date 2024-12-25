

class RNG:
    def __init__(self, seed):
        self.seed = seed
        self.value = seed

    @staticmethod
    def mix(value1, value2):
        return value1 ^ value2

    @staticmethod
    def prune(value):
        return value % 16777216

    def next(self):
        # Version 1

        operand1 = self.value * 64
        operand1 = self.mix(self.value, operand1)
        operand1 = self.prune(operand1)

        operand2 = int(operand1 / 32)
        operand2 = self.mix(operand1, operand2)
        operand2 = self.prune(operand2)

        operand3 = operand2 * 2048
        operand3 = self.mix(operand2, operand3)
        operand3 = self.prune(operand3)

        self.value = operand3
        return self.value

    def get(self):
        return self.value
