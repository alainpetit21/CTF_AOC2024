import re

from engine.Challenge import Challenge


class ChallengeDay4C2(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.result = 0

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)

        for y in range(len(self.data)):
            self.data[y] = self.data[y].strip()

    def check_kernel(self, pos, kernel, direction):
        data = self.data
        xmas = "MAS"
        count = 0

        match = True
        for idx in range(len(xmas)):
            if not data[pos[1] + kernel[1] + (direction[1] * idx)][pos[0] + kernel[0] + (direction[0] * idx)] == xmas[idx]:
                match = False
                break

        if match:
            count += 1

        return count

    def run(self):
        data = self.data
                    # ((kernelX, kernelY), (incX, incY))
        kernels = [((-1, -1), (1, 1)),
                   ((1, -1), (-1, 1)),
                   ((-1, 1), (1, -1)),
                   ((1, 1), (-1, -1))]

        count = 0
        for y in range(1, len(data) - 1):
            for x in range(1, len(data[0])-1):
                count = 0
                for kernel in kernels:
                    count += self.check_kernel((x, y), kernel[0], kernel[1])

                if count == 2:
                    self.result += 1

        return self.result
