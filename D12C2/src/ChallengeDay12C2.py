from engine.Challenge import Challenge

class Tile:
    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3

    MAX_WIDTH = 0
    MAX_HEIGHT = 0

    def __init__(self, x, y, val):
        self.val = val
        self.pos = (x,y)
        self.walls = [True, True, True, True]    # East, South, West, North
        self.adj_tiles: [Tile] = [None, None, None, None]
        self.area = 1
        self.all_in_group = []
        self.accounted = False

    def set_adjacent_tile(self, tile, direct):
        self.adj_tiles[direct] = tile
        self.walls[direct] = False

    def is_in_group(self, x, y):
        ret_sub = False
        ret = self.pos[0] == x and self.pos[1] == y

        for tile in self.adj_tiles:
            ret_sub = tile.is_in_group(x, y)

        return ret or ret_sub

class ChallengeDay12C2(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.result = 0
        self.groups = []
        self.checked = []
        self.tile_array: [[Tile]] = []

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)

        for y in range(len(self.data)):
            self.data[y] = self.data[y].strip()

        Tile.MAX_WIDTH = len(self.data[0])
        Tile.MAX_HEIGHT = len(self.data)

    def _find_area(self, tile, list_group) -> int:
        if self.checked[tile.pos[1]][tile.pos[0]]:
            return 0
        if tile.accounted:
            return 0

        self.checked[tile.pos[1]][tile.pos[0]] = True

        nb_added = 1
        list_group.append(tile)
        tile.all_in_group = list_group
        tile.accounted = True

        for adj_tile in tile.adj_tiles:
            if adj_tile:
                nb_added += self._find_area(adj_tile, list_group)

        return nb_added

    def find_area(self, tile, list_group):
        self.checked = [[False for _ in range(len(self.data[0]))] for _ in range(len(self.data))]
        tile.area = self._find_area(tile, list_group)

    def run(self):
        for y in range(len(self.data)):
            row_tile = []
            for x in range(len(self.data[0])):
                row_tile.append(Tile(x, y, self.data[y][x]))
            self.tile_array.append(row_tile)

        for y in range(len(self.tile_array)):
            for x in range(len(self.tile_array[0])):
                this_tile: Tile = self.tile_array[y][x]

                # East
                if x < Tile.MAX_WIDTH - 1:
                    east_tile: Tile = self.tile_array[y][x + 1]
                    if east_tile.val == this_tile.val:
                        this_tile.set_adjacent_tile(east_tile, Tile.EAST)
                        east_tile.set_adjacent_tile(this_tile, Tile.WEST)

                # South
                if y < Tile.MAX_HEIGHT - 1:
                    south_tile: Tile = self.tile_array[y + 1][x]
                    if south_tile.val == this_tile.val:
                        this_tile.set_adjacent_tile(south_tile, Tile.SOUTH)
                        south_tile.set_adjacent_tile(this_tile, Tile.NORTH)

                # West
                if x > 0:
                    west_tile: Tile = self.tile_array[y][x - 1]
                    if west_tile.val == this_tile.val:
                        this_tile.set_adjacent_tile(west_tile, Tile.WEST)
                        west_tile.set_adjacent_tile(this_tile, Tile.EAST)

                # North
                if y > 0:
                    north_tile: Tile = self.tile_array[y - 1][x]
                    if north_tile.val == this_tile.val:
                        this_tile.set_adjacent_tile(north_tile, Tile.NORTH)
                        north_tile.set_adjacent_tile(this_tile, Tile.SOUTH)

        for y in range(len(self.tile_array)):
            for x in range(len(self.tile_array[0])):
                all_in_group = []
                self.find_area(self.tile_array[y][x], all_in_group)
                if len(all_in_group) > 0:
                    self.groups.append(all_in_group)

        self.result = 0
        for i, group in enumerate(self.groups):
            area = len(group)
            perimeter = 0
            for tile in group:
                perimeter += sum(tile.walls)
            sub_total = area * perimeter
            print(f"{i}: {area}:{perimeter} = {sub_total}")
            self.result += sub_total

        self.result = 0
        for i, group in enumerate(self.groups):
            area = len(group)

            min_x = min(group, key=lambda tile: tile.pos[0])
            max_x = max(group, key=lambda tile: tile.pos[0])
            min_y = min(group, key=lambda tile: tile.pos[1])
            max_y = max(group, key=lambda tile: tile.pos[1])

            north_sides = []
            for i in range(min_x, max_x):
                if i == min_x:
                    north_sides.append()

            nb_side = 0
            for direction in sides:
                nb_side += len(direction)

            sub_total = area * nb_side
            self.result += sub_total

        return self.result
