from D13C2.src.ChallengeDay13C2 import ChallengeDay13C2


def test_loading():
    chall = ChallengeDay13C2("./data/example.txt")

    assert chall.data[0][0] == 'B'
    assert chall.data[1][0] == 'B'


def test_interpret_data():
    chall = ChallengeDay13C2("./data/example.txt")
    chall.interpret_data()

    assert len(chall.machines) == 4


def test_result():
    chall = ChallengeDay13C2("./data/example.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 875318608908


if __name__ == '__main__':
    test_loading()
    test_interpret_data()
    test_result()

    print("Passed all tests")
