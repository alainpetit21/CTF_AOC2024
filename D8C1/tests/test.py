from D8C1.src.ChallengeDay8C1 import ChallengeDay8C1


def test_loading():
    chall = ChallengeDay8C1("./data/example.txt")

    assert chall.data[0][0] == '.'
    assert chall.data[1][0] == '.'


def interpret_data():
    chall = ChallengeDay8C1("./data/example.txt")
    chall.interpret_data()

    assert len(chall.dic_antennas) == 2


def test_result():
    chall = ChallengeDay8C1("./data/example.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 14


if __name__ == '__main__':
    test_loading()
    test_result()

    print("Passed all tests")
