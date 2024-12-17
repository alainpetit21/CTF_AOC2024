from D15C1.src.Object import Object


class Wall(Object):
    def move(self, direction:list[tuple[int,int]]) -> bool:
        return False

    def __str__(self):
        return "#"
