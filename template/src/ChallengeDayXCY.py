from engine.Challenge import Challenge


class ChallengeDayXCY(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.result = 0

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)

    def run(self):
        return self.result
