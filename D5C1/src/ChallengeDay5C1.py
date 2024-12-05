import re

from engine.Challenge import Challenge


class ChallengeDay5C1(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.result = 0
        self.start_manual_line = 0
        self.rules = []
        self.manuals = []
        self.is_correct = []

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)

        for y in range(len(self.data)):
            self.data[y] = self.data[y].strip()

    def load_rule_set(self):

        for line in self.data:
            if line == "":
                self.start_manual_line += 1
                break

            group = line.split('|')
            self.rules.append((int(group[0]), int(group[1])))
            self.start_manual_line += 1

    def load_update_manuals(self):
        for line in self.data[self.start_manual_line:]:
            group = line.split(',')
            manual = [int(val) for val in group]
            self.manuals.append(manual)

    def is_manual_correct(self, manual : [int]):

        for rule in self.rules:
            rule1 = rule[0]
            rule2 = rule[1]

            try:
                idx_1 = manual.index(rule1)
                idx_2 = manual.index(rule2)
            except ValueError:
                continue

            if idx_1 > idx_2:
                return False

        return True

    def is_manuals_correct(self):
        for manual in self.manuals:
            self.is_correct.append(self.is_manual_correct(manual))

    def run(self):
        all_results = []
        for i, manual in enumerate(self.manuals):
            if self.is_correct[i]:
                all_results.append(manual[len(manual)//2])

        self.result = sum(all_results)
        return self.result
