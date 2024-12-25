from collections import Counter
from engine.Challenge import Challenge


class ChallengeDay11C2(Challenge):
    def __init__(self, filename=None, nb_blinks=75):
        super().__init__(filename)
        self.result = 0
        self.stones = []
        self.nb_blinks = nb_blinks

        self.stone_counts = Counter()  # Track counts of identical stones

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)

        numbers = self.data[0].split(' ')
        self.stone_counts = Counter(int(x) for x in numbers)

    @staticmethod
    def split_even_size(num):
        s = str(num)
        mid = len(s) // 2
        return int(s[:mid]), int(s[mid:])

    def run(self):
        for i in range(self.nb_blinks):
            print(f"Running blink {i} of {self.nb_blinks} : {i / self.nb_blinks * 100:.2f}%")
            new_stone_counts = Counter()

            for stone, count in self.stone_counts.items():
                if stone == 0:
                    new_stone_counts[1] += count
                elif len(str(stone)) % 2 == 0:
                    left, right = self.split_even_size(stone)
                    new_stone_counts[left] += count
                    new_stone_counts[right] += count
                else:
                    new_stone_counts[stone * 2024] += count

            self.stone_counts = new_stone_counts

        self.result = sum(self.stone_counts.values())
        return self.result
