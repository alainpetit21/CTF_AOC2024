from D10C2.src.ChallengeDay10C2 import ChallengeDay10C2


def test_loading():
    chall = ChallengeDay10C2("./data/example.txt")

    assert chall.data[0][0] == '8'
    assert chall.data[1][0] == '7'


def test_interpret_data():
    chall = ChallengeDay10C2("./data/example.txt")
    chall.interpret_data()

    assert chall.numbers[0][0] == 8
    assert chall.numbers[1][0] == 7


def test_result():
    chall = ChallengeDay10C2("./data/example1.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 3

    chall = ChallengeDay10C2("./data/example2.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 13

    chall = ChallengeDay10C2("./data/example3.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 227

    chall = ChallengeDay10C2("./data/example.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 81


if __name__ == '__main__':
    test_loading()
    test_interpret_data()
    test_result()

    print("Passed all tests")
