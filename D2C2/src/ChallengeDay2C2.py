from engine.Challenge import Challenge


class ChallengeDay2C2(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.result = 0
        self.report_is_inc = []
        self.data_num = []
        self.report_is_safe = []

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)

        for row in self.data:
            group = row.strip().split(" ")
            self.data_num.append([int(val) for val in group])

    def detect_safe(self, row):
        is_inc = row[1] - row[0] > 0

        prev = row[0]
        for val in row[1:]:
            if is_inc:
                if val <= prev:
                    return False
            else:
                if val >= prev:
                    return False

            if abs(val - prev) > 3:
                return False

            prev = val

        return True

    def run(self):
        self.report_is_safe = [False for _ in range(len(self.data_num))]

        for i in range(len(self.data_num)):
            row = self.data_num[i]
            is_safe = self.detect_safe(row)

            if not is_safe:
                # try to remove each val and see if it passes
                for j, val in enumerate(row):
                    new_row = row[:]
                    del new_row[j]
                    new_is_safe = self.detect_safe(new_row)

                    if new_is_safe:
                        self.report_is_safe[i] = True
                        break
            else:
                self.report_is_safe[i] = True

        for i, v in enumerate(self.report_is_safe):
            if v:
                self.result += 1

        return self.result
