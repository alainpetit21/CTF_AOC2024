from itertools import combinations

from D8C2.src.Antenna import Antenna
from D8C2.src.Antinode import Antinode
from engine.Challenge import Challenge


class ChallengeDay8C2(Challenge):
    WIDTH = 0
    HEIGHT = 0

    def __init__(self, filename=None):
        super().__init__(filename)
        self.result = 0
        self.map = []
        self.dic_antennas = {}
        self.antinodes = []

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)

        self.HEIGHT = len(self.data)
        self.WIDTH = len(self.data[0])

        for y in range(self.HEIGHT):
            row = []
            for x in range(self.WIDTH):
                if self.data[y][x] != '.':
                    antenna = Antenna(x, y, self.data[y][x])
                    row.append(antenna)

                    if self.data[y][x] not in self.dic_antennas:
                        self.dic_antennas[self.data[y][x]] = []

                    self.dic_antennas[self.data[y][x]].append(antenna)
                else:
                    row.append(None)

            self.map.append(row)

    def already_antinode(self, x, y):
        for antinode in self.antinodes:
            if x == antinode.x and y == antinode.y:
                return True

        return False

    def run(self):
        for freq in self.dic_antennas:
            all_antennas = self.dic_antennas[freq]
            all_comparaison = list(combinations(all_antennas, 2))

            for pair in all_comparaison:
                d_x = pair[1].x - pair[0].x
                d_y = pair[1].y - pair[0].y

                # Directly on Pair[0]
                if not self.already_antinode(pair[0].x, pair[0].y):
                    self.antinodes.append(Antinode(pair[0].x, pair[0].y))
                if not self.already_antinode(pair[1].x, pair[1].y):
                    self.antinodes.append(Antinode(pair[1].x, pair[1].y))

                # All before
                antinode = Antinode(pair[0].x - d_x, pair[0].y - d_y)
                while (0 <= antinode.x < self.WIDTH) and (0 <= antinode.y < self.HEIGHT):
                    if not self.map[antinode.y][antinode.x]:
                        self.map[antinode.y][antinode.x] = antinode
                        self.antinodes.append(antinode)
                    else:
                        if isinstance(self.map[antinode.y][antinode.x], Antenna):
                            if not self.already_antinode(antinode.x, antinode.y):
                                self.antinodes.append(antinode)
                    antinode = Antinode(antinode.x - d_x, antinode.y - d_y)

                # All After
                antinode = Antinode(pair[1].x + d_x, pair[1].y + d_y)
                while (0 <= antinode.x < self.WIDTH) and (0 <= antinode.y < self.HEIGHT):
                    if not self.map[antinode.y][antinode.x]:
                        self.map[antinode.y][antinode.x] = antinode
                        self.antinodes.append(antinode)
                    else:
                        if isinstance(self.map[antinode.y][antinode.x], Antenna):
                            if not self.already_antinode(antinode.x, antinode.y):
                                self.antinodes.append(antinode)
                    antinode = Antinode(antinode.x + d_x, antinode.y + d_y)

        self.antinodes = sorted(self.antinodes)
        self.result += len(self.antinodes)
        return self.result
