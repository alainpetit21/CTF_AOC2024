import heapq
from copy import deepcopy

from matplotlib import pyplot as plt, patches
from matplotlib.collections import PatchCollection

from D20C1.src.Tile import Tile
from engine.Challenge import Challenge


class ChallengeD20C1(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.result = 0
        self.tilemap: [[Tile]] = []
        self.width_tiles = 0
        self.height_tiles = 0

        self.start = None
        self.goal = None

        self.cheats = {}
        self.nb_steps = 0
        self.nb_cheats = 0

    def init_tilemap(self, tilemap, data, width_tiles, height_tiles) -> ((int,int), (int,int)):
        start = None
        goal = None

        for y in range(len(tilemap)):
            for x in range(len(tilemap[0])):
                if data[y][x] == '#':
                    tilemap[y][x].is_wall = True
                    continue

                if data[y][x] == 'S':
                    tilemap[y][x].is_start = True
                    start = (x, y)

                if data[y][x] == 'E':
                    tilemap[y][x].is_goal = True
                    goal = (x, y)

                if (x < width_tiles - 1) and (data[y][x + 1] != '#'):
                    tilemap[y][x].set_east(tilemap[y][x + 1])

                if (y < height_tiles - 1) and (data[y + 1][x] != '#'):
                    tilemap[y][x].set_south(tilemap[y + 1][x])

                if (x > 0) and (data[y][x - 1] != '#'):
                    tilemap[y][x].set_west(tilemap[y][x - 1])

                if (y > 0) and (data[y - 1][x] != '#'):
                    tilemap[y][x].set_north(tilemap[y - 1][x])

        return start, goal

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)

        for y in range(len(self.data)):
            self.data[y] = self.data[y].strip()

        # Once we have an 2D array of idx (00-03) we can use that to create another 2D array of Tile objects this time.
        width_tiles = self.width_tiles = len(self.data[0])
        height_tiles = self.height_tiles = len(self.data)
        self.tilemap = [[Tile(x, y) for x in range(width_tiles)] for y in range(height_tiles)]
        self.start, self.goal = self.init_tilemap(self.tilemap, self.data, width_tiles, height_tiles)

    def visualize_map(self, map_tiles, width_tiles, height_tiles, path=None):
        # Some initialisations
        fig, ax = plt.subplots()
        patchs = []
        arrow_params = dict(facecolor='black', shrink=0.05, headwidth=5, headlength=5)

        # Loop through all tiles to draw it
        for j in range(height_tiles):
            for i in range(width_tiles):
                tile = map_tiles[j][i]

                # Draw a rectangle for the each tile
                rect = patches.Rectangle((i, j), 1, 1, fill=False)
                patchs.append(rect)

                # Draw a "S" for start and a "G" for goal
                if tile.is_start:
                    ax.text(i + 0.5, j + 0.5, 'S', color='green', ha='center', va='center', fontsize=16, weight='bold')
                if tile.is_goal:
                    ax.text(i + 0.5, j + 0.5, 'G', color='red', ha='center', va='center', fontsize=16, weight='bold')

                # Draw The arrows depending if there are not any wall (opening) on the north, east, south and west side
                if tile.tile_east:
                    ax.annotate('', xy=(i + 1, j + 0.5), xytext=(i + 0.5, j + 0.5), arrowprops=arrow_params)
                if tile.tile_west:
                    ax.annotate('', xy=(i, j + 0.5), xytext=(i + 0.5, j + 0.5), arrowprops=arrow_params)
                if tile.tile_north:
                    ax.annotate('', xy=(i + 0.5, j), xytext=(i + 0.5, j + 0.5), arrowprops=arrow_params)
                if tile.tile_south:
                    ax.annotate('', xy=(i + 0.5, j + 1), xytext=(i + 0.5, j + 0.5), arrowprops=arrow_params)

        collection = PatchCollection(patchs, match_original=True)
        ax.add_collection(collection)

        # Draw the path if provided
        if path:
            path_coords = [((tile_tup[0].x + 0.5), (tile_tup[0].y + 0.5)) for tile_tup in path]
            path_coords_x, path_coords_y = zip(*path_coords)
            ax.plot(path_coords_x, path_coords_y, color='blue', linewidth=10)

        # Prepare the plot to be display in a new window
        plt.xlim(-1, width_tiles)
        plt.ylim(-1, height_tiles)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.gca().invert_yaxis()  # Invert y axis to match array indexing
        plt.grid(True)
        plt.ioff()  # Ensure interactive mode is off
        plt.show()

    def pathfinding(self, map_tiles, pos_start, pos_goal) -> list:
        # get start and goal tile objects
        start_tile = map_tiles[pos_start[1]][pos_start[0]]
        goal_tile = map_tiles[pos_goal[1]][pos_goal[0]]

        # Priority queue to store the tiles to be processed
        queue = []
        start_tile.distance = 0
        heapq.heappush(queue, (start_tile.distance, start_tile, (1, 0)))  # None for no initial direction))

        # Dictionary to store the previous tile for each tile
        previous_tiles = {start_tile.get_id(): None}  # (previous_tile, direction)

        # Loop while the queue is not empty
        while queue:
            # Pop from the priority queue
            current_distance, current_tile, current_direction = heapq.heappop(queue)

            # If we are at destination, break
            if current_tile is goal_tile:
                break

            # Loop Through all the current tile neighbours
            for neighbor in current_tile.neighbor:
                if neighbor is not None:
                    # Calculate direction of movement
                    direction = (neighbor.x - current_tile.x, neighbor.y - current_tile.y)

                    # Assuming each move has a cost of 1
                    distance = current_distance + 1

                    # If the neighbor has a greater distance than the calculated distance, update it
                    if distance < neighbor.distance:
                        neighbor.distance = distance
                        heapq.heappush(queue, (neighbor.distance, neighbor, direction))
                        previous_tiles[neighbor.get_id()] = (current_tile, direction)

        # Reconstruct the path, from previous_tiles array
        path = []
        tile_tup = (goal_tile, (1, 0))
        while True:
            # print(f"Adding: {tile_tup[0].x};{tile_tup[0].y}")
            path.append(tile_tup)
            tile_tup = previous_tiles[tile_tup[0].get_id()]

            if tile_tup is None:
                break
            tile = tile_tup
        path.reverse()

        # return the path
        return path

    def run(self):
        # Run the pathfinding first to know what is the real nb_step without cheats
        path = self.pathfinding(self.tilemap, self.start, self.goal)
        # self.visualize_map(self.tilemap, self.width_tiles, self.height_tiles, path)

        self.nb_steps = len(path) - 1

        for y in range(self.height_tiles):
            # Some debug printout
            total = self.height_tiles * self.width_tiles
            current = y * self.width_tiles
            print(f"{current / total * 100.0}")

            for x in range(self.width_tiles):

                if self.tilemap[y][x].is_wall:
                    # make copy of the data input
                    data_with_cheat = [[self.data[y][x] for x in range(self.width_tiles)] for y in range(self.height_tiles)]
                    data_with_cheat[y][x] = '.'

                    # make copy of the timemap
                    tilemap_with_cheat = self.tilemap = [[Tile(x, y) for x in range(self.width_tiles)] for y in range(self.height_tiles)]
                    self.init_tilemap(tilemap_with_cheat, data_with_cheat, self.width_tiles, self.height_tiles)
                    tilemap_with_cheat[y][x] = Tile(x, y, tile=self.tilemap[y][x])
                    tilemap_with_cheat[y][x].is_wall = False

                    path = self.pathfinding(tilemap_with_cheat, self.start, self.goal)
                    # self.visualize_map(self.tilemap, self.width_tiles, self.height_tiles, path)
                    nb_steps_cheat = len(path) - 1

                    if nb_steps_cheat < self.nb_steps:
                        self.cheats[(x, y)] = self.nb_steps - nb_steps_cheat

        self.nb_cheats = len(self.cheats) - 1
        self.result = len({key: value for key, value in self.cheats.items() if value >= 100})
        return self.result
