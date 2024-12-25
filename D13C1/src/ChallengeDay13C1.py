from engine.Challenge import Challenge
import re
from sympy import symbols, Eq, solve


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

    @staticmethod
    def minimize_cost(dx_a, dy_a, c_a, dx_b, dy_b, c_b, x_prize, y_prize):
        # Minimize:3a+b
        # 27a+58b=2211
        # 65a+17b=4587

        # Isolate one variable in express the equation in factor of the other
        # b = (2211 - 27a) / 58

        # Substitute b in second equation :
        # 65a + 17 * ((2211 - 27a) / 58) = 4587   ... all terms gets divided by 17 to give :
        # 65a/17 + (2211 - 27a) / 58 = 4587/17  ... all terms gets multiplied by 58 to give :
        # (3770a/17) + 2211 - 27a = 266046/17 ... move 2211 to the right to give :
        # (3770a/17) - 27a = 266046/17 - 2211 ... all terms multiplied by 17 to give :
        # 3770a - 459a = 266046 - 37587 ... performed substractions to give :
        # 3311a = 228459 ... all gets divided by 3311 to give :
        # a = 69

        # Replace a in the other equation
        # 65a+17b=4587 ... replace a to give :
        # 65*69 + 17b = 4587 ... perfromed some calculation
        # 4485 + 17b = 4587 ... move numbers to the right
        # 17b = 4587 - 4485 ... do the math on the right :
        # 17b = 102 ... all divided by 17
        # b = 102/17 = 6

        # Minimized Cost function
        # Cost=3a+b = 3*69 + 6
        # 207 + 6
        # 213

        # translate that into a sympy equation

        # Define variables
        a, b = symbols('a b', integer=True, positive=True)

        # Equations for X and Y
        eq1 = Eq(dx_a * a + dx_b * b, x_prize)
        eq2 = Eq(dy_a * a + dy_b * b, y_prize)

        # Solve for 'a' and 'b'
        solutions = solve((eq1, eq2), (a, b))

        # When only one solution is found the return is a dict.
        if isinstance(solutions, dict):
            # Check for non-negative integers
            if all(val >= 0 for val in solutions.values()):
                cost = c_a * solutions[a] + c_b * solutions[b]
                return solutions, cost

        # When only zero, two or more solution is found the return is a list.
        elif isinstance(solutions, list):
            min_cost = float('inf')
            best_solution = None

            for sol in solutions:
                if isinstance(sol, dict) and all(val >= 0 for val in sol.values()):
                    cost = c_a * sol[a] + c_b * sol[b]
                    if cost < min_cost:
                        min_cost = cost
                        best_solution = sol
            return best_solution, min_cost

        return None, None

    def run(self):
        for cpt, machine in enumerate(self.machines):
            print(f"Processing machine {cpt} of {len(self.machines)}: {cpt/len(self.machines)*100:.2f}")

            sol, min_cost = self.minimize_cost(machine.move_button_a[0], machine.move_button_a[1], 3,
                                               machine.move_button_b[0], machine.move_button_b[1], 1,
                                               machine.prize_loc[0], machine.prize_loc[1])

            if sol:
                self.result += min_cost

        return self.result
