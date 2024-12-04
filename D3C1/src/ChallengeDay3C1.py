import re

from engine.Challenge import Challenge


class ChallengeDay3C1(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.input = None
        self.result = 0
        self.report_is_inc = []
        self.data_num = []
        self.report_is_safe = []

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)
        self.input = "".join(self.data).strip()

    def run(self):
        numbers = []
        muls = []
        group = re.findall(r"mul\(\d+,\d+\)", self.input)

        for vals in group:
            group2 = re.findall(r"\d+", vals)
            number_tup = (int(group2[0]), int(group2[1]))
            numbers.append(number_tup)
            muls.append(number_tup[0] * number_tup[1])

        self.result = sum(muls)

        return self.result
