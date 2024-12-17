from abc import abstractmethod

class Object:
    DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    DIR_EAST = 0
    DIR_SOUTH = 1
    DIR_WEST = 2
    DIR_NORTH = 3
    theWorld = None

    def __init__(self, x, y, world):
        self.pos = [x, y]
        Object.theWorld = world

    @abstractmethod
    def can_move(self, direction: int) -> bool:
        ...

    @abstractmethod
    def do_move(self, direction: int):
        ...

    def render(self):
        Object.theWorld.set_at(self.pos[0], self.pos[1], self)
