

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

    def move(self, direction: int) -> bool:
        ret = True
        newPos_x, newPos_y = self.pos
        newPos_x += Object.DIRECTIONS[direction][0]
        newPos_y += Object.DIRECTIONS[direction][1]

        object_at = Object.theWorld.get_at(newPos_x, newPos_y)
        if object_at is not None:
            ret = object_at.move(direction)

        if ret:
            self.pos = (newPos_x, newPos_y)

        return ret

    def render(self, char):
        Object.theWorld.set_at(self.pos[0], self.pos[1], self)
