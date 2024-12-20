from D19C1.src.ChallengeD19C1 import (ChallengeD19C1)


def test_loading():
    chall = ChallengeD19C1("./data/example.txt")

    assert chall.data[0][0] == 'r'
    assert chall.data[0][1] == ','


def test_interpret_data():
    chall = ChallengeD19C1("./data/example.txt")
    chall.interpret_data()

    assert len(chall.towels) == 8

    assert len(chall.towels[0]) == 3
    assert len(chall.towels[-1]) == 1

    assert len(chall.patterns) == 8


def test_result():
    chall = ChallengeD19C1("./data/example.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 6


if __name__ == '__main__':
    test_loading()
    test_interpret_data()
    test_result()

    print("Passed all tests")
