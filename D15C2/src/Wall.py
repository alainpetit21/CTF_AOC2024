from D15C2.src.Object import Object


class Wall(Object):
    def can_move(self, direction: list[tuple[int, int]]) -> bool:
        return False

    def __str__(self):
        return "#"
