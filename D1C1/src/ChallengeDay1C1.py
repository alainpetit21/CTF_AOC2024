from engine.Challenge import Challenge


class ChallengeDay1C1(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)

    def interpret_data(self, data_inj: [str] = None):
        data = super().interpret_data(data_inj)

        #TODO do something with data
        for row in data:
            ...
