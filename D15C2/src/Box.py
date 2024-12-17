from D15C2.src.Object import Object


class Box(Object):
    def __str__(self):
        return "O"

    def can_move(self, direction: int) -> bool:
        ret = True
        newPos_x, newPos_y = self.pos
        newPos_x += Object.DIRECTIONS[direction][0]
        newPos_y += Object.DIRECTIONS[direction][1]

        # Moving left or right
        if direction % 2 == 0:
            object_at = Object.theWorld.get_at(newPos_x, newPos_y)

            if object_at is not None:
                if object_at is not self:
                    ret = object_at.can_move(direction)
                else:
                    object_at = Object.theWorld.get_at(newPos_x - 1, newPos_y)
                    if object_at is not None:
                        if object_at is not self:
                            ret = object_at.can_move(direction)
        # Moving Up and Down
        else:
            object_at = Object.theWorld.get_at(newPos_x, newPos_y)
            object_at2 = Object.theWorld.get_at(newPos_x+1, newPos_y)

            ret1 = ret2 = True
            if object_at:
                ret1 = object_at.can_move(direction)
            if object_at2:
                ret2 = object_at2.can_move(direction)
            ret = ret1 and ret2

        return ret

    def do_move(self, direction:int):
        newPos_x, newPos_y = self.pos
        newPos_x += Object.DIRECTIONS[direction][0]
        newPos_y += Object.DIRECTIONS[direction][1]


        # Moving left or right
        if direction % 2 == 0:
            object_at = Object.theWorld.get_at(newPos_x, newPos_y)

            if object_at is not None:
                if object_at is not self:
                    object_at.do_move(direction)
                else:
                    object_at = Object.theWorld.get_at(newPos_x - 1, newPos_y)
                    if object_at is not None:
                        if object_at is not self:
                            object_at.do_move(direction)
        # Moving Up and Down
        else:
            object_at = Object.theWorld.get_at(newPos_x, newPos_y)
            object_at2 = Object.theWorld.get_at(newPos_x+1, newPos_y)

            if object_at:
                object_at.do_move(direction)
            if object_at2 and (object_at is not object_at2):
                object_at2.do_move(direction)

        self.pos = (newPos_x, newPos_y)


