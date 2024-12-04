from D4C1.src.ChallengeDay4C1 import ChallengeDay4C1


def test_loading():
    chall = ChallengeDay4C1("./data/example.txt")

    assert chall.data[0][0] == 'M'
    assert chall.data[1][0] == 'M'


def test_result():
    chall = ChallengeDay4C1("./data/example.txt")
    chall.interpret_data()
    chall.run()

    assert chall.result == 18


if __name__ == '__main__':
    test_loading()
    test_result()

    print("Passed all tests")
