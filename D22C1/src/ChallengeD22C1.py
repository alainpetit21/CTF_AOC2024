from D22C1.src.RNG import RNG
from engine.Challenge import Challenge


class ChallengeD22C1(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.result = 0
        self.seeds = []
        self.numbers: [RNG] = []

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)

        for val in self.data:
            self.seeds.append(int(val))
            self.numbers.append(RNG(int(val)))

    def run(self):
        for number in self.numbers:
            for i in range(2000):
                number.next()

            self.result += number.get()

        return self.result
