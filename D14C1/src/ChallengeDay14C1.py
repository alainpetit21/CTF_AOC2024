from engine.Challenge import Challenge
import re

class Robot:
    def __init__(self, x, y, vx, vy):
        self.pos = [x, y]
        self.vel = [vx, vy]

    def manage(self):

        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        self.pos[0] %= ChallengeDay14C1.WIDTH
        self.pos[1] %= ChallengeDay14C1.HEIGHT

    def __repr__(self):
        return f"Robot at {self.pos[0]}:{self.pos[1]}"


class ChallengeDay14C1(Challenge):
    WIDTH = 101
    HEIGHT = 103

    def __init__(self, filename=None, width=101, height=103):
        super().__init__(filename)
        ChallengeDay14C1.WIDTH = width
        ChallengeDay14C1.HEIGHT = height
        self.result = 0
        self.robots = []

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)

        for y in range(len(self.data)):
            self.data[y] = self.data[y].strip()

        it_data = iter(self.data)
        for line in it_data:
            robot = re.findall(r"^p=(\d*),(\d*) v=(-?\d*),(-?\d*)$", line)[0]
            robot = Robot(int(robot[0]), int(robot[1]),int(robot[2]), int(robot[3]))
            self.robots.append(robot)

    def execute_move(self):
        for i in range(100):
            for robot in self.robots:
                robot.manage()

    def calculate_per_quadrant(self) -> (int, int, int, int):
        quadrant_dimension_x = [(-1, ChallengeDay14C1.WIDTH//2),
                                (ChallengeDay14C1.WIDTH//2, ChallengeDay14C1.WIDTH),
                                (-1, ChallengeDay14C1.WIDTH//2),
                                (ChallengeDay14C1.WIDTH//2, ChallengeDay14C1.WIDTH)]
        quadrant_dimension_y = [(-1, ChallengeDay14C1.HEIGHT//2),
                                (-1, ChallengeDay14C1.HEIGHT//2),
                                (ChallengeDay14C1.HEIGHT//2, ChallengeDay14C1.HEIGHT),
                                (ChallengeDay14C1.HEIGHT//2, ChallengeDay14C1.HEIGHT)]
        res = [0, 0, 0, 0]
        for i in range(4):
            for robot in self.robots:
                quad_x = quadrant_dimension_x[i]
                quad_y = quadrant_dimension_y[i]

                if quad_x[0] < robot.pos[0] < quad_x[1]:
                    if quad_y[0] < robot.pos[1] < quad_y[1]:
                        res[i] += 1

        return res[0], res[1], res[2], res[3]

    def run(self):
        self.execute_move()
        res = self.calculate_per_quadrant()
        self.result = res[0]*res[1]*res[2]*res[3]

        return self.result
