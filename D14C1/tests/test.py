from D14C1.src.ChallengeDay14C1 import ChallengeDay14C1


def test_loading():
    chall = ChallengeDay14C1("./data/example.txt", 11, 7)

    assert chall.data[0][0] == 'p'
    assert chall.data[1][0] == 'p'


def test_interpret_data():
    chall = ChallengeDay14C1("./data/example.txt", 11, 7)
    chall.interpret_data()


def test_result():
    chall = ChallengeDay14C1("./data/example.txt", 11, 7)
    chall.interpret_data()

    chall.run()
    assert chall.result == 12


if __name__ == '__main__':
    test_loading()
    test_interpret_data()
    test_result()

    print("Passed all tests")
