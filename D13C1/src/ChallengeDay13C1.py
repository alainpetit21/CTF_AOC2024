from engine.Challenge import Challenge
import re

class Machine:
    def __init__(self, move_button_a, move_button_b, prize_loc):
        self.move_button_a = move_button_a
        self.move_button_b = move_button_b
        self.prize_loc = prize_loc


class ChallengeDay13C1(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.result = 0
        self.machines = []

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)

        for y in range(len(self.data)):
            self.data[y] = self.data[y].strip()

        it_data = iter(self.data)
        for line in it_data:
            group_button_A = re.findall(r"^Button A: X\+(\d*), Y\+(\d*)$", line)[0]
            line = next(it_data, None)

            group_button_B = re.findall(r"^Button B: X\+(\d*), Y\+(\d*)$", line)[0]
            line = next(it_data, None)

            group_prize = re.findall(r"^Prize: X=(\d*), Y=(\d*)$", line)[0]
            next(it_data, None)

            machine = Machine((int(group_button_A[0]), int(group_button_A[1])),
                              (int(group_button_B[0]), int(group_button_B[1])),
                              (int(group_prize[0]), int(group_prize[1])))

            self.machines.append(machine)

    def run(self):


        return self.result
