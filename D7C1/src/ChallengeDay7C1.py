from D7C1.src.Operation import Operation
from engine.Challenge import Challenge


class ChallengeDay7C1(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.result = 0
        self.operations = []

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)

        for line in self.data:
            parts = line.split(': ')
            result = int(parts[0])

            operands = parts[1].split(" ")
            operands = [int(x) for x in operands]
            self.operations.append(Operation(result, operands))

    def do_operation(self, operators, operands):
        assert len(operators) == (len(operands) - 1)

        if len(operands) == 1:
            return operands[0]

        ret = self.do_operation(operators[:-1], operands[:-1])

        if operators[-1] == '+':
            result = ret + operands[-1]
        elif operators[-1] == '*':
            result = ret * operands[-1]
        else:
            assert False

        return result

    @staticmethod
    def convert_operator(operator, nb_element):
        binary_string = format(operator, f'0{nb_element}b')
        custom_string = ''.join('*' if bit == '1' else '+' for bit in binary_string)
        return list(custom_string)

    def run(self):
        for operation in self.operations:
            nb_operators = len(operation.operands)-1
            max_operator = (2 ** nb_operators)

            for operator in range(max_operator):
                lst_operations = self.convert_operator(operator, nb_operators)
                result = self.do_operation(lst_operations, operation.operands)

                if result == operation.result:
                    self.result += result
                    break

        return self.result
