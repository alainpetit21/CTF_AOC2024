
class Tile:
    def __init__(self, x, y):
        self.tile_east = None
        self.tile_west = None
        self.tile_north = None
        self.tile_south = None

        self.neighbor = [None, None, None, None]

        self.is_start = False
        self.is_goal = False
        self.is_wall = False

        self.distance = float('inf')  # Distance from start, initially set to infinity
        self.x = x
        self.y = y

    def set_north(self, tile):
        self.tile_north = tile
        self.neighbor[0] = self.tile_north

    def set_east(self, tile):
        self.tile_east = tile
        self.neighbor[1] = self.tile_east

    def set_south(self, tile):
        self.tile_south = tile
        self.neighbor[2] = self.tile_south

    def set_west(self, tile):
        self.tile_west = tile
        self.neighbor[3] = self.tile_west

    def __lt__(self, other):
        return self.distance < other.distance

    def get_id(self):
        return self.x, self.y

