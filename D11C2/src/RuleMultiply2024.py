from D11C1.src.Rule import Rule


class RuleMultiply2024(Rule):
    def __init__(self):
        super().__init__()

    def __call__(self, *args, **kwargs):
        return True, [args[0]*2024]
