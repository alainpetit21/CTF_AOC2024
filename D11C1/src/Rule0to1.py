from D11C1.src.Rule import Rule


class Rule0to1(Rule):
    def __init__(self):
        super().__init__()

    def __call__(self, *args, **kwargs):
        if args[0] == 0:
            return True, [1]

        return False, None
