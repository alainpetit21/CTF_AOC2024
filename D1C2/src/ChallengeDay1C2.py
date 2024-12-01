from engine.Challenge import Challenge
import re
from collections import Counter


class ChallengeDay1C2(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.list1 = []
        self.list2 = []
        self.muls = []
        self.result = 0

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)

        for row in self.data:
            group = re.findall(r"(\d*)\s*(\d*)\n?", row)
            group = group[0]
            self.list1.append(int(group[0]))
            self.list2.append(int(group[1]))

    def run(self):
        counter = Counter(self.list2)

        for val in self.list1:
            nb_occurrence = counter[val]
            self.muls.append(val * nb_occurrence)

        self.result = sum(self.muls)
        return self.result
