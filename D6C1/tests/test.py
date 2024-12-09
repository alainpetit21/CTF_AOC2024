from D6C1.src.ChallengeDay6C1 import ChallengeDay6C1


def test_loading():
    chall = ChallengeDay6C1("./data/example.txt")

    assert chall.data[0][0] == '.'
    assert chall.data[1][0] == '.'


def interpret_data():
    chall = ChallengeDay6C1("./data/example.txt")
    chall.interpret_data()

    assert chall.guard_pos[0] == 4
    assert chall.guard_pos[1] == 6


def test_result():
    chall = ChallengeDay6C1("./data/example.txt")
    chall.interpret_data()
    chall.run()

    assert chall.result == 41


if __name__ == '__main__':
    test_loading()
    test_result()

    print("Passed all tests")
