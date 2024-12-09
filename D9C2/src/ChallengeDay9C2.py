from engine.Challenge import Challenge


class ChallengeDay9C2(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.result = 0
        self.decoded = []
        self.newData = []
        self.mem_block = []

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)

        for y in range(len(self.data)):
            self.data[y] = self.data[y].strip()

    def decode_input(self):
        self.decoded = []

        cpt_length = 0
        for i, val in enumerate(self.data[0]):

            # This is for character mode
            if i % 2 == 0:
                data = int(i // 2)
                length = int(val)
            # This is for space mode
            else:
                data = '.'
                length = int(val)

            self.mem_block.append((cpt_length, data, length))
            cpt_length+= length


    def find_free_spot(self, size):
        for item in self.mem_block:
            if item[2] >= size and item[1] == '.':
                return item

        return None

    def replace_bloc(self, bloc, item):
        idx_to = self.mem_block.index(bloc)
        idx_from = self.mem_block.index(item)

        self.mem_block[idx_to] = (bloc[0], item[1], item[2])
        self.mem_block[idx_from] = (item[0], '.', item[2])

        if bloc[2] - item[2] > 0:
            self.mem_block.insert(idx_to+1, (bloc[0]+item[2], '.', bloc[2] - item[2]))

    def merge_empties(self):
        i = 0
        while i < len(self.mem_block) - 1:
            item = self.mem_block[i]
            next = self.mem_block[i+1]

            if item[1] == next[1]:
                item = (item[0], item[1], item[2] + next[2])
                self.mem_block[i] = item
                del self.mem_block[i+1]
                i= 0

            i += 1

    def render(self):
        for item in self.mem_block:
            for i in range(item[2]):
                self.newData.append(item[1])

    def compress_filesystem(self):
        """
        last = None
        start_pos = None

        # pass 1 find empty spot length structure format (loc, size)
        for i, val in enumerate(self.decoded):
            if val != last:
                if last is None:
                    start_pos = i
                    last = val
                else:
                    self.mem_block.append((start_pos, last, i - start_pos))
                    start_pos = i
                    last = val
        else:
            self.mem_block.append((start_pos, last, len(self.decoded) - start_pos))
        """
        temp = reversed(self.mem_block)
        for item in temp:
            if item[1] != '.':
                bloc = self.find_free_spot(item[2])
                if bloc is not None:
                    if bloc[0] > item[0]:
                        continue

                    self.replace_bloc(bloc, item)

        self.merge_empties()
        self.render()

    def calculate_checksum(self):

        for i, val in enumerate(self.newData):
            if val != '.':
                num_val = int(val)
                self.result += (i*num_val)

    def run(self):
        self.decode_input()
        self.compress_filesystem()
        self.calculate_checksum()

        return self.result
