from D12C1.src.ChallengeDay12C1 import ChallengeDay12C1


def test_loading():
    chall = ChallengeDay12C1("./data/example.txt")

    assert chall.data[0][0] == 'A'
    assert chall.data[1][0] == 'B'


def test_interpret_data():
    chall = ChallengeDay12C1("./data/example.txt")
    chall.interpret_data()


def test_result():
    chall = ChallengeDay12C1("./data/example.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 140

    chall = ChallengeDay12C1("./data/example2.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 772

    chall = ChallengeDay12C1("./data/example3.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 1930


if __name__ == '__main__':
    test_loading()
    test_interpret_data()
    test_result()

    print("Passed all tests")
