
class Antenna:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

    def __repr__(self):
        return f"Antenna {self.x};{self.y}"
