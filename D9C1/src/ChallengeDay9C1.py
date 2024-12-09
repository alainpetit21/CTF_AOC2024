from engine.Challenge import Challenge


class ChallengeDay9C1(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.result = 0
        self.decoded = []
        self.endPt = None
        self.newData = []
        self.idxEnd = None

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)

        for y in range(len(self.data)):
            self.data[y] = self.data[y].strip()

    def decode_input(self):

        self.decoded = []

        for i, val in enumerate(self.data[0]):

            # This is for character mode
            if i % 2 == 0:
                data = int(i // 2)
                length = int(val)
            # This is for space mode
            else:
                data = '.'
                length = int(val)

            for j in range(length):
                self.decoded.append(data)

        self.endPt = list(self.decoded[-1::-1])
        self.idxEnd = len(self.decoded)-1

    def move_nextEndPt(self):
        self.idxEnd -= 1
        self.endPt = self.endPt[1:]
        while self.endPt[0] == '.':
            self.idxEnd -= 1
            self.endPt = self.endPt[1:]

    def compress_filesystem(self):
        for i in range(len(self.decoded)):
            if i > self.idxEnd:
                break

            if self.decoded[i] == '.':
                val = self.endPt[0]
                self.newData.append(val)
                self.move_nextEndPt()
            else:
                self.newData.append(self.decoded[i])

        for i in range(len(self.newData), len(self.decoded)):
            self.newData.append('.')

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

