from D22C2.src.RNG import RNG
from engine.Challenge import Challenge


class ChallengeD22C2(Challenge):
    def __init__(self, filename=None, max_iterations=2000):
        super().__init__(filename)
        self.result = 0
        self.MAX_ITER = max_iterations
        self.seeds = []
        self.numbers: [RNG] = []

        self.all_results: [[int]] = []
        self.all_results_mod_10: [[int]] = []
        self.deltas: [[int]] = []

        self.highest_price: [int] = []
        self.hh_price = 0
        self.sequence_of_4 = []

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)

        for val in self.data:
            self.seeds.append(int(val))
            self.numbers.append(RNG(int(val)))

    @staticmethod
    def find_sequence_in_list(lst, sequence):
        lst_str = ','.join(map(str, lst))
        seq_str = ','.join(map(str, sequence))
        index = lst_str.find(seq_str)
        if index != -1:
            return lst_str[:index].count(',')  # Calculate the starting index
        return -1

    def run_old(self):
        for idx, number in enumerate(self.numbers):
            self.all_results.append([])
            self.all_results_mod_10.append([])
            self.deltas.append([])

            for cpt in range(self.MAX_ITER):
                self.all_results[idx].append(number.get())
                self.all_results_mod_10[idx].append(self.all_results[idx][cpt] % 10)

                if cpt > 0:
                    self.deltas[idx].append(self.all_results_mod_10[idx][cpt] - self.all_results_mod_10[idx][cpt - 1])

                number.next()

            self.highest_price.append(max(self.all_results_mod_10[idx]))

        self.hh_price = max(self.highest_price)
        wich_row = self.highest_price.index(self.hh_price)
        which_iteration = self.all_results_mod_10[wich_row].index(self.hh_price)
        which_iteration = self.all_results_mod_10[wich_row].index(self.hh_price, which_iteration + 1)
        self.sequence_of_4 = [self.deltas[wich_row][which_iteration - 4],
                              self.deltas[wich_row][which_iteration - 3],
                              self.deltas[wich_row][which_iteration - 2],
                              self.deltas[wich_row][which_iteration - 1]]

        return self.result

    def run(self):
        for idx, number in enumerate(self.numbers):
            self.all_results.append([])
            self.all_results_mod_10.append([])
            self.deltas.append([])

            for cpt in range(self.MAX_ITER):
                self.all_results[idx].append(number.get())
                self.all_results_mod_10[idx].append(self.all_results[idx][cpt] % 10)

                if cpt > 0:
                    self.deltas[idx].append(self.all_results_mod_10[idx][cpt] - self.all_results_mod_10[idx][cpt - 1])

                number.next()

            self.highest_price.append(max(self.all_results_mod_10[idx]))

        highest = {}
        tot_ite = 19 ** 4
        cpt_it = 0
        for it1 in range(-9, 10):
            for it2 in range(-9, 10):
                for it3 in range(-9, 10):
                    for it4 in range(-9, 10):
                        cpt_it += 1
                        sequence_of_4 = (it1, it2, it3, it4)
                        print(f"Trying {cpt_it / tot_ite * 100}")

                        highest[sequence_of_4] = 0

                        for idx, number in enumerate(self.numbers):
                            idx_in_row = self.find_sequence_in_list(self.deltas[idx], sequence_of_4)

                            if idx_in_row != -1:
                                value = self.all_results_mod_10[idx][idx_in_row + 4]
                                highest[sequence_of_4] += value

        self.sequence_of_4 = max(highest, key=highest.get)
        value = highest[self.sequence_of_4]
        print(f"{value} using {self.sequence_of_4}")
        self.result = value
        return self.result
