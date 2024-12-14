from engine.Challenge import Challenge
import re


class Robot:
    def __init__(self, x, y, vx, vy):
        self.pos = [x, y]
        self.vel = [vx, vy]

    def manage(self):

        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        self.pos[0] %= ChallengeDay14C2.WIDTH
        self.pos[1] %= ChallengeDay14C2.HEIGHT

    def __repr__(self):
        return f"Robot at {self.pos[0]}:{self.pos[1]}"


class ChallengeDay14C2(Challenge):
    WIDTH = 101
    HEIGHT = 103

    def __init__(self, filename=None, width=101, height=103):
        super().__init__(filename)
        ChallengeDay14C2.WIDTH = width
        ChallengeDay14C2.HEIGHT = height
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

    def dump_image(self, it):
        dump = [['.' for _ in range(ChallengeDay14C2.WIDTH)] for _ in range(ChallengeDay14C2.HEIGHT)]

        for robot in self.robots:
            dump[robot.pos[1]][robot.pos[0]] = '8'

        with open("out.txt", "a") as file_out:
            file_out.writelines(f"{it}" + '\n')
            for line in dump:
                file_out.writelines("".join(line) + '\n')

    def execute_move(self):
        for i in range(10000):
            for robot in self.robots:
                robot.manage()

            self.dump_image(i)

    def run(self):
        self.execute_move()

        return self.result
