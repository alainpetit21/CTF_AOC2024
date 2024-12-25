from D11C1.src.Rule0to1 import Rule0to1
from D11C1.src.RuleMultiply2024 import RuleMultiply2024
from D11C1.src.RuleSplitOnEvenSize import RuleSplitOnEvenSize
from engine.Challenge import Challenge


class ChallengeDay11C1(Challenge):
    def __init__(self, filename=None, nb_blinks=25):
        super().__init__(filename)
        self.result = 0
        self.stones = []
        self.nb_blinks = nb_blinks
        self.rules = [Rule0to1(), RuleSplitOnEvenSize(), RuleMultiply2024()]

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)

        numbers = self.data[0].split(' ')
        self.stones = [int(x) for x in numbers]

    def run(self):
        for i in range(self.nb_blinks):
            temp_stones = []
            for stone in self.stones:
                for rule in self.rules:
                    processed, stones_ret = rule(stone)

                    if processed:
                        for stone_ret in stones_ret:
                            temp_stones.append(stone_ret)
                        break

            self.stones = temp_stones

        self.result = len(self.stones)
        return self.result
