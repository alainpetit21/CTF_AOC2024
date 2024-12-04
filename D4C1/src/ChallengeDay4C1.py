import re

from engine.Challenge import Challenge


class ChallengeDay4C1(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.result = 0

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)

        for y in range(len(self.data)):
            self.data[y] = self.data[y].strip()

    def check_dir(self, direction):
        data = self.data
        xmas = "XMAS"
        count = 0
        for y in range(len(data)):
            if y + (direction[1] * 3) < 0:
                continue
            elif y + (direction[1] * 3) >= len(data):
                continue

            for x in range(len(data[0])):
                if x + (direction[0] * 3) < 0:
                    continue
                if x + (direction[0] * 3) >= len(data[0]):
                    continue

                match = True
                for idx in range(len(xmas)):

                    if not data[y + (direction[1] * idx)][x + (direction[0] * idx)] == xmas[idx]:
                        match = False
                        break

                if match:
                    count += 1

        return count

    def run(self):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)]

        all_res = []
        for direction in directions:
            all_res.append(self.check_dir(direction))

        self.result = sum(all_res)
        return self.result
