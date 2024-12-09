from engine.Challenge import Challenge


class ChallengeDay6C2(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.ALL_DIR = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        self.result = 0
        self.guard_pos = None
        self.guard_dir = None

        self.new_obstacle = []
        self.all_path_lines = []
        self.last_path_line = []

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

    def lines_are_connected(self, line1, line2):
        connected = False

        if all(p[0] == line1[0][0] for p in line1) and all(p[0] == line2[0][0] for p in line2):
            return False
        if all(p[1] == line1[0][1] for p in line1) and all(p[1] == line2[0][1] for p in line2):
            return False

        # Déterminer si les deux lignes sont verticales
        if not (all(p[0] == line1[0][0] for p in line1) and all(p[0] == line2[0][0] for p in line2)):
            # Vérifiez s'il y a un chevauchement sur l'axe vertical (y)
            y1_range = range(min(p[1] for p in line1), max(p[1] for p in line1) + 1)
            y2_range = range(min(p[1] for p in line2), max(p[1] for p in line2) + 1)
            return bool(set(y1_range) & set(y2_range))  # Intersection non vide des ranges

        # Déterminer si les deux lignes sont horizontales
        if not (all(p[1] == line1[0][1] for p in line1) and all(p[1] == line2[0][1] for p in line2)):
            # Vérifiez s'il y a un chevauchement sur l'axe horizontal (x)
            x1_range = range(min(p[0] for p in line1), max(p[0] for p in line1) + 1)
            x2_range = range(min(p[0] for p in line2), max(p[0] for p in line2) + 1)
            return bool(set(x1_range) & set(x2_range))  # Intersection non vide des ranges

        # Les lignes doivent se connecter par leurs extrémités
        return line1[-1] == line2[0]

    def is_closed_rectangle(self, min_3, min_2, min_1, last):

        if not (self.lines_are_connected(min_3, min_2) and
                self.lines_are_connected(min_2, min_1) and
                self.lines_are_connected(min_1, last) and
                self.lines_are_connected(last, min_3)):
            return False

        # Vérifiez les dimensions : les côtés opposés doivent avoir la même longueur
        def line_length(line):
            return abs(line[-1][0] - line[0][0]) + abs(line[-1][1] - line[0][1])

        return line_length(min_3) == line_length(min_1) and line_length(min_2) == line_length(last)

    def detect_loop_in_last_4_lines(self, last_line, all_lines):
        if len(all_lines) < 3:
            return False

        min_3 = all_lines[-3]
        min_2 = all_lines[-2]
        min_1 = all_lines[-1]
        last = last_line

        if self.is_closed_rectangle(min_3, min_2, min_1, last):
            return True

        return False

    def automate_guard_for_max_step(self, run_max):
        MAX_X = len(self.data[0])
        MAX_Y = len(self.data[1])
        data = self.data
        pos = self.guard_pos
        direction = self.guard_dir
        seen = [[False for _ in range(MAX_X)] for _ in range(MAX_Y)]

        seen[pos[1]][pos[0]] = True
        self.last_path_line.append(pos)

        for i in range(run_max):
            v_direction = self.ALL_DIR[direction]
            next_tile = pos[0] + v_direction[0], pos[1] + v_direction[1]

            if not ((0 <= next_tile[0] < MAX_X) and (0 <= next_tile[1] < MAX_Y)):
                return sum(sum(row) for row in seen), i
            elif data[next_tile[1]][next_tile[0]] == '#' or data[next_tile[1]][next_tile[0]] == 'O':
                self.last_path_line.append(pos)
                self.all_path_lines.append(self.last_path_line)
                self.last_path_line = [pos]
                direction += 1
                direction %= 4
                continue

            pos = next_tile
            seen[pos[1]][pos[0]] = True
            self.last_path_line.append(pos)
            if self.detect_loop_in_last_4_lines(self.last_path_line, self.all_path_lines):
                self.new_obstacle.append((pos[0]+v_direction[0], pos[1]+v_direction[1]))

        return sum(sum(row) for row in seen), 5000

    def run(self):
        MAX_X = len(self.data[0])
        MAX_Y = len(self.data[1])

        found_this_run, nb_steps = self.automate_guard_for_max_step(5000)
        self.result = len(self.new_obstacle)
        return self.result

    def run_v1_brute_force_with_lower_seen_spot(self):

        standard, i = self.automate_guard_for_max_step(5000)
        print(f"Standard for this path: {standard} within {i} steps")

        for y in range(len(self.data)):
            for x in range(len(self.data[0])):
                saved = self.data[y]
                self.data[y] = saved[:x] + 'O' + saved[x + 1:]
                found_this_run, nb_steps = self.automate_guard_for_max_step(5000)

                if nb_steps == 5000:
                    if found_this_run < standard:
                        print(f"Found loop {found_this_run}, setting obs. at {x}, {y}")
                        self.new_obstacle.append((x, y))

                self.data[y] = saved

        self.result = len(self.new_obstacle)
        return self.result
