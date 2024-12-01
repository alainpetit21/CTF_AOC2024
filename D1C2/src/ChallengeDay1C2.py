from engine.Challenge import Challenge
import re


class ChallengeDay1C2(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.list1 = []
        self.list2 = []
        self.diffs = []
        self.result = 0

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)

        for row in self.data:
            group = re.findall(r"(\d*)\s*(\d*)\n?", row)
            group = group[0]
            self.list1.append(int(group[0]))
            self.list2.append(int(group[1]))

    def run(self):
        self.list1 = sorted(self.list1)
        self.list2 = sorted(self.list2)

        for i in range(len(self.list1)):
            val1 = self.list1[i]
            val2 = self.list2[i]

            self.diffs.append(abs((val2-val1)))

        self.result = sum(self.diffs)

        return self.result
