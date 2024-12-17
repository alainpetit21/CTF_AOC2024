from ctypes import cast

from D15C2.src.Object import Object


class Robot(Object):
    def __str__(self):
        return "@"

    def can_move(self, direction: int) -> bool:
        ret = True
        newPos_x, newPos_y = self.pos
        newPos_x += Object.DIRECTIONS[direction][0]
        newPos_y += Object.DIRECTIONS[direction][1]

        if newPos_y == 4 and newPos_x == 7:
            print("debug")

        object_at = Object.theWorld.get_at(newPos_x, newPos_y)
        if object_at is not None:
            ret = object_at.can_move(direction)

        return ret

    def do_move(self, direction:int):
        newPos_x, newPos_y = self.pos
        newPos_x += Object.DIRECTIONS[direction][0]
        newPos_y += Object.DIRECTIONS[direction][1]

        object_at = Object.theWorld.get_at(newPos_x, newPos_y)
        if object_at is not None:
            object_at.do_move(direction)

        self.pos = (newPos_x, newPos_y)


