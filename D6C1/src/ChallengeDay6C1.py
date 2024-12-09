from engine.Challenge import Challenge


class ChallengeDay6C1(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.ALL_DIR = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        self.result = 0
        self.guard_pos = None
        self.guard_dir = None

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)

        for y in range(len(self.data)):
            self.data[y] = self.data[y].strip()

        self.guard_pos = self.find_guard()
        self.guard_dir = 0

    def find_guard(self) -> (int, int):
        for y in range(len(self.data)):
            for x in range(len(self.data[0])):
                if self.data[y][x] == '^':
                    return x, y

    def automate_guard_for_max_step(self, run_max):
        MAX_X = len(self.data[0])
        MAX_Y = len(self.data[1])
        data = self.data
        pos = self.guard_pos
        direction = self.guard_dir
        seen = [[False for _ in range(MAX_X)] for _ in range(MAX_Y)]

        seen[pos[1]][pos[0]] = True

        print(f"Round X with {run_max} move\n"+("="*100))
        for i in range(run_max):
            v_direction = self.ALL_DIR[direction]
            next_tile = pos[0]+v_direction[0], pos[1]+v_direction[1]

            if not ((0 <= next_tile[0] < MAX_X) and (0 <= next_tile[1] < MAX_Y)):
                break
            elif data[next_tile[1]][next_tile[0]] == '#':
                print(f"Rotate")
                direction += 1
                direction %= 4
                continue

            pos = next_tile
            seen[pos[1]][pos[0]] = True
            print(f"Move to {pos}; ")

        return sum(sum(row) for row in seen)

    def run(self):
        found_last_run = -1
        found_this_run = 0

        run_max = 10000
        while found_last_run != found_this_run:
            found_last_run = found_this_run
            run_max += 100

            found_this_run = self.automate_guard_for_max_step(run_max)

        self.result = found_this_run
        return self.result

