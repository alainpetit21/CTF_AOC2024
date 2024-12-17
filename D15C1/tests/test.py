from D15C1.src.ChallengeDay15C1 import ChallengeDay15C1


def test_loading():
    chall = ChallengeDay15C1("./data/example.txt")

    assert chall.data[0][0] == '#'
    assert chall.data[1][0] == '#'


def test_interpret_data():
    chall = ChallengeDay15C1("./data/example.txt")
    chall.interpret_data()


def test_result():
    chall = ChallengeDay15C1("./data/example2.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 2028

    chall = ChallengeDay15C1("./data/example.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 10092


if __name__ == '__main__':
    test_loading()
    test_interpret_data()
    test_result()

    print("Passed all tests")
