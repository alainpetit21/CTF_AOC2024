from D7C2.src.Operation import Operation
from engine.Challenge import Challenge


class ChallengeDay7C2(Challenge):
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
        elif operators[-1] == '|':
            result = int(str(ret) + str(operands[-1]))
        else:
            assert False

        return result

    @staticmethod
    def convert_operator(operator, nb_element, base):
        # Step 1: Convert the number to the specified base
        digits = []
        while operator > 0:
            digits.append(operator % base)
            operator //= base

        # If the number is 0, represent it as a single '0' digit
        if not digits:
            digits = [0]

        # Reverse the digits to get the correct base representation
        base_representation = ''.join(map(str, reversed(digits)))

        # Step 2: Pad the base string to the desired length
        padded_base_string = base_representation.zfill(nb_element)

        # Step 3: Replace each digit with custom symbols (e.g., '*' for 1, '+' for 0)
        # You can define your own mapping
        custom_mapping = {'0': '+', '1': '*', '2': '|'}
        custom_string = ''.join(custom_mapping[digit] for digit in padded_base_string)

        return list(custom_string)

    def run(self):

        for cpt, operation in enumerate(self.operations):
            nb_operators = len(operation.operands)-1
            max_operator = (3 ** nb_operators)

            for operator in range(max_operator):
                lst_operations = self.convert_operator(operator, nb_operators, 3)
                result = self.do_operation(lst_operations, operation.operands)

                if result == operation.result:
                    self.result += result
                    break

            print(f"{cpt} of {len(self.operations)} = {cpt/len(self.operations)*100}%")

        return self.result
