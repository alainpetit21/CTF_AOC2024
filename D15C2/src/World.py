from typing import Optional

from D15C2.src.Box import Box
from D15C2.src.Object import Object
from D15C2.src.Robot import Robot
from D15C2.src.Wall import Wall


class World:
    WIDTH = 0
    HEIGHT = 0

    def __init__(self, data):
        World.WIDTH = len(data[0] * 2)
        World.HEIGHT = len(data)
        self.internal_world: list[list[Optional[Object]]] = \
            [[None for _ in range(World.WIDTH)] for _ in range(World.HEIGHT)]
        self.the_robot: Optional[Robot] = None
        self.walls = []
        self.boxes = []

    def load_data(self, data):
        for y in range(World.HEIGHT):
            for x in range(World.WIDTH//2):
                match data[y][x]:
                    case '#':
                        wall = Wall(x*2, y, self)
                        self.internal_world[y][x*2] = wall
                        self.internal_world[y][x*2+1] = wall
                        self.walls.append(wall)
                    case 'O':
                        box = Box(x*2, y, self)
                        self.internal_world[y][x*2] = box
                        self.internal_world[y][x*2+1] = box
                        self.boxes.append(box)
                    case '@':
                        robot = Robot(x*2, y, self)
                        self.internal_world[y][x*2] = robot
                        self.the_robot = robot

    def get_at(self, x, y):
        try:
            return self.internal_world[y][x]
        except IndexError as e:
            print("toto")

        return None

    def set_at(self, x, y, obj):
        self.internal_world[y][x] = obj
        self.internal_world[y][x+1] = obj

    def render_new_positions(self):
        self.internal_world = [[None for _ in range(World.WIDTH)] for _ in range(World.HEIGHT)]

        for wall in self.walls:
            self.internal_world[wall.pos[1]][wall.pos[0]] = wall
            self.internal_world[wall.pos[1]][wall.pos[0]+1] = wall

        for box in self.boxes:
            self.internal_world[box.pos[1]][box.pos[0]] = box
            self.internal_world[box.pos[1]][box.pos[0]+1] = box

        self.internal_world[self.the_robot.pos[1]][self.the_robot.pos[0]] = self.the_robot

    def __repr__(self):
        return f"World(HEIGHT={self.HEIGHT}, WIDTH={self.WIDTH})"

    def __str__(self):
        string = "The World\n" + "=" * 100 + "\n"

        for y in range(World.HEIGHT):
            x = 0
            while x < World.WIDTH:
                object_at = self.internal_world[y][int(x)]

                if object_at is not None:
                    ret = object_at.__str__()
                    string += ret
                else:
                    string += '.'

                x += 1

            string += '\n'

        return string
