from engine.Challenge import Challenge
import re


class ChallengeDay3C2(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.input = None
        self.result = 0

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)
        self.input = "".join(self.data).strip()

    def run(self):
        numbers = []
        muls = []
        group = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", self.input)

        in_do = True
        for vals in group:
            if in_do:
                if vals == "don't()":
                    in_do = False
                    continue

                if vals == "do()":
                    in_do = True
                    continue

                group2 = re.findall(r"\d+", vals)
                number_tup = (int(group2[0]), int(group2[1]))
                numbers.append(number_tup)
                muls.append(number_tup[0] * number_tup[1])
            else:
                if vals == "do()":
                    in_do = True

        self.result = sum(muls)

        return self.result
