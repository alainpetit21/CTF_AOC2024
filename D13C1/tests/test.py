from D13C1.src.ChallengeDay13C1 import ChallengeDay13C1


def test_loading():
    chall = ChallengeDay13C1("./data/example.txt")

    assert chall.data[0][0] == 'B'
    assert chall.data[1][0] == 'B'


def test_interpret_data():
    chall = ChallengeDay13C1("./data/example.txt")
    chall.interpret_data()

    assert len(chall.machines) == 4


def test_result():
    chall = ChallengeDay13C1("./data/example.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 480


if __name__ == '__main__':
    test_loading()
    test_interpret_data()
    test_result()

    print("Passed all tests")
