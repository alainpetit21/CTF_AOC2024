from engine.Challenge import Challenge


class ChallengeD23C2(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.result = 0
        self.computers = set()
        self.connections = set()
        self.connections3 = set()
        self.connections3_t = set()
        self.clusters = {}

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

    def build_cluster(self):

        for computer in self.computers:
            self.clusters[computer] = set()

        for computer in self.computers:
            for group in self.connections3:
                if computer in group:
                    for element in group:
                        self.clusters[group[0]].add(element)
                    for element in group:
                        self.clusters[group[1]].add(element)
                    for element in group:
                        self.clusters[group[2]].add(element)

        print(self.clusters)

    def run(self):
        self.build_connection_of_3()
        self.build_cluster()
        self.result = ",".join(set(sorted(self.all_view_computers)))
        return self.result
