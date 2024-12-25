from D11C1.src.Rule import Rule


class RuleSplitOnEvenSize(Rule):
    def __init__(self):
        super().__init__()

    def __call__(self, *args, **kwargs):
        str_stone = str(args[0])
        len_string = len(str_stone)
        if len_string % 2 == 0:
            half_len = len_string // 2

            part1 = str_stone[:half_len]
            part2 = str_stone[half_len:]
            print(f"{str_stone} gets split in {part1} and {part2}")
            return True, [int(part1), int(part2)]

        return False, None
