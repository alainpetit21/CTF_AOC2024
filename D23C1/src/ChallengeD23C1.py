from engine.Challenge import Challenge


class ChallengeD23C1(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.result = 0
        self.computers = set()
        self.connections = set()
        self.connections3 = set()
        self.connections3_t = set()

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)

        for line in self.data:
            computers = line.split('-')
            self.computers.add(computers[0])
            self.computers.add(computers[1])

            self.connections.add(tuple(sorted(computers)))
        # print(self.connections)

    def build_connection_of_3(self):
        for connection in self.connections:
            first = connection[0]
            second = connection[1]

            for inner_connection in self.connections:
                inner_first = inner_connection[0]
                inner_second = inner_connection[1]

                if inner_first == first and inner_second == second:
                    continue

                if inner_first == first:
                    test_tuple = tuple(sorted([second, inner_second]))
                    if test_tuple in self.connections:
                        self.connections3.add(tuple(set(sorted((first, second, inner_first, inner_second)))))

                if inner_second == second:
                    test_tuple = tuple(sorted([first, inner_first]))
                    if test_tuple in self.connections:
                        self.connections3.add(tuple(set(sorted((first, second, inner_first, inner_second)))))

    def build_connection_of_3_with_T(self):
        for connection in self.connections3:
            for element in connection:
                if element.startswith("t"):
                    self.connections3_t.add(connection)

        # print(self.connections3_t)

    def run(self):
        self.build_connection_of_3()
        self.build_connection_of_3_with_T()
        self.result = len(self.connections3_t)
        return self.result
