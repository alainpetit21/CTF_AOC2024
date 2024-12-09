from D10C2.src.ChallengeDay10C2 import ChallengeDay10C2


def test_loading():
    chall = ChallengeDay10C2("./data/example.txt")

    assert chall.data[0][0] == '.'
    assert chall.data[1][0] == '.'


def interpret_data():
    chall = ChallengeDay10C2("./data/example.txt")
    chall.interpret_data()


def test_result():
    chall = ChallengeDay10C2("./data/example.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 6


if __name__ == '__main__':
    test_loading()
    test_result()

    print("Passed all tests")
