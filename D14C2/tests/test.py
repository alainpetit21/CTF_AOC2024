from D14C2.src.ChallengeDay14C2 import ChallengeDay14C2


def test_loading():
    chall = ChallengeDay14C2("./data/example.txt")

    assert chall.data[0][0] == 'p'
    assert chall.data[1][0] == 'p'


def test_interpret_data():
    chall = ChallengeDay14C2("./data/example.txt")
    chall.interpret_data()


def test_result():
    chall = ChallengeDay14C2("./data/example.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 0


if __name__ == '__main__':
    test_loading()
    test_interpret_data()
    test_result()

    print("Passed all tests")
