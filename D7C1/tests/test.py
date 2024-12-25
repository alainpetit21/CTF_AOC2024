from D7C1.src.ChallengeDay7C1 import ChallengeDay7C1


def test_loading():
    chall = ChallengeDay7C1("./data/example.txt")

    assert chall.data[0][0] == '1'
    assert chall.data[1][0] == '3'


def interpret_data():
    chall = ChallengeDay7C1("./data/example.txt")
    chall.interpret_data()

    assert len(chall.operations) == 9


def test_result():
    chall = ChallengeDay7C1("./data/example.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 3749


if __name__ == '__main__':
    test_loading()
    test_result()

    print("Passed all tests")
