class Operation:
    OPERATORS = ['+', '*']

    def __init__(self, result: int, operands: [int]):
        self.result = result
        self.operands = operands
