from engine.Challenge import Challenge
import re


class ChallengeDay2C1(Challenge):
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

            self.report_is_safe[i] = is_safe

        for v in self.report_is_safe:
            if v:
                self.result += 1

        return self.result

    def run_old(self):

        for row in self.data_num:
            if row[1] - row[0] > 0:
                self.report_is_inc.append(True)
            else:
                self.report_is_inc.append(False)

        self.report_is_safe = [True for _ in range(len(self.data_num))]
        for i in range(len(self.data_num)):
            row = self.data_num[i]
            is_inc = self.report_is_inc[i]

            prev = row[0]
            for val in row[1:]:
                if is_inc:
                    if val < prev:
                        self.report_is_safe[i] = False
                        break
                else:
                    if val > prev:
                        self.report_is_safe[i] = False
                        break
                if abs(val - prev) > 3:
                    self.report_is_safe[i] = False
                    break
                if abs(val - prev) == 0:
                    self.report_is_safe[i] = False
                    break

                prev = val

        for v in self.report_is_safe:
            if v:
                self.result += 1

        return self.result
