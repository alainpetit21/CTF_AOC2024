class Antinode:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Antinode {self.x};{self.y}"

    def __lt__(self, other):
        if self.y < other.y:
            return True
        elif self.y == other.y:
            if self.x < other.x:
                return True

        return False
