from engine.Challenge import Challenge


class ChallengeD19C1(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.result = 0
        self.towels = []
        self.patterns = []
        self.patterns_combo = {}

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)

        for y in range(len(self.data)):
            self.data[y] = self.data[y].strip()

        line: str = self.data[0]
        self.towels = line.split(", ")
        self.towels = sorted(self.towels, key=lambda x: len(x), reverse=True)

        for pattern in self.data[2:]:
            self.patterns.append(pattern)

    def recursive_check(self, remaining, solvable):
        if remaining in solvable:
            return solvable[remaining]
        if not remaining:
            return True

        for towel in self.towels:
            if remaining.startswith(towel):
                if self.recursive_check(remaining[len(towel):], solvable):
                    solvable[remaining] = True
                    return True

        solvable[remaining] = False
        return False

    def run(self):
        for pattern in self.patterns:
            solvable = {}

            ret = self.recursive_check(pattern, solvable)

            if ret:
                print(f"Pattern '{pattern}' is doable")
                self.result += 1
            else:
                print(f"Pattern '{pattern}' is not doable")
                if pattern in self.patterns_combo.keys():
                    self.patterns_combo.pop(pattern)

        return self.result
