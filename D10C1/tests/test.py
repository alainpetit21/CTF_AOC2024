from D10C1.src.ChallengeDay10C1 import ChallengeDay10C1


def test_loading():
    chall = ChallengeDay10C1("./data/example.txt")

    assert chall.data[0][0] == '.'
    assert chall.data[1][0] == '.'


def interpret_data():
    chall = ChallengeDay10C1("./data/example.txt")
    chall.interpret_data()


def test_result():
    chall = ChallengeDay10C1("./data/example.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 6


if __name__ == '__main__':
    test_loading()
    test_result()

    print("Passed all tests")
