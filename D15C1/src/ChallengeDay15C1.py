from typing import Optional

from D15C1.src.Object import Object
from D15C1.src.Robot import Robot
from D15C1.src.World import World
from engine.Challenge import Challenge


class ChallengeDay15C1(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.world_data = []
        self.commands = []
        self.the_world: Optional[World] = None
        self.the_robot: Optional[Robot] = None

        self.result = 0

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)

        for y in range(len(self.data)):
            self.data[y] = self.data[y].strip()

        for line in self.data:
            if line == "":
                ...
            elif line[0] == "#":
                self.world_data.append(line)
            elif line[0] in "<^>v":
                self.commands.append(line)

        self.the_world: World = World(self.world_data)
        self.the_world.load_data(self.world_data)
        self.commands = "".join(self.commands)
        self.the_robot = self.the_world.the_robot
        print(self.the_world)

    def run(self):
        commands_dirs = ['>', 'v', '<', '^']

        for command in self.commands:
            # print(command)
            command_dir = commands_dirs.index(command)
            self.the_robot.move(command_dir)
            self.the_world.render_new_positions()
            # print(self.the_world)

        for box in self.the_world.boxes:
            self.result += (box.pos[1] * 100 + box.pos[0])

        return self.result
