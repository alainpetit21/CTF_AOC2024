from engine.Challenge import Challenge


class ChallengeDay5C2(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.fixed_manuals = []
        self.result = 0
        self.start_manual_line = 0
        self.rules = []
        self.manuals = []
        self.correct_manuals = []
        self.incorrect_manuals = []
        self.correct_manuals_idx = []
        self.incorrect_manuals_idx = []

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
                return False, ((rule1, idx_1), (rule2, idx_2))

        return True, ()

    def classify_manuals(self):
        for i, manual in enumerate(self.manuals):
            if self.is_manual_correct(manual)[0]:
                self.correct_manuals.append(manual)
                self.correct_manuals_idx.append(i)
            else:
                self.incorrect_manuals.append(manual)
                self.incorrect_manuals_idx.append(i)

    def fix_incorrect_manuals(self):
        for idx, manual in enumerate(self.incorrect_manuals):
            fixed, error = self.is_manual_correct(manual)

            if fixed:
                print(f"fixed {idx+1} of {len(self.incorrect_manuals)}: {self.incorrect_manuals_idx[idx]}= {self.incorrect_manuals[idx]}")
                self.fixed_manuals.append(manual)
                del self.incorrect_manuals[idx]
                return False

            # print(f"incorrect found {idx} of {len(self.incorrect_manuals)}: {self.incorrect_manuals_idx[idx]}= {self.incorrect_manuals[idx]}")
            idx_1 = error[0][1]
            page_1 = error[0][0]
            idx_2 = error[1][1]
            page_2 = error[1][0]
            self.incorrect_manuals[idx][idx_2] = page_1
            self.incorrect_manuals[idx][idx_1] = page_2
            return False

        return True

    def run(self):
        all_results = []

        self.load_rule_set()
        self.load_update_manuals()
        self.classify_manuals()

        while not self.fix_incorrect_manuals():
            pass

        for i, manual in enumerate(self.fixed_manuals):
            all_results.append(manual[len(manual)//2])

        self.result = sum(all_results)
        return self.result
