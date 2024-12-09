from D9C2.src.ChallengeDay9C2 import ChallengeDay9C2


def test_loading():
    chall = ChallengeDay9C2("./data/example.txt")

    assert chall.data[0][0] == '.'
    assert chall.data[1][0] == '.'


def interpret_data():
    chall = ChallengeDay9C2("./data/example.txt")
    chall.interpret_data()


def test_result():
    chall = ChallengeDay9C2("./data/example.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 6


if __name__ == '__main__':
    test_loading()
    test_result()

    print("Passed all tests")
