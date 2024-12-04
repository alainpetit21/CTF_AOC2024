from D3C1.src.ChallengeDay3C1 import ChallengeDay3C1


def test_loading():
    chall = ChallengeDay3C1("./data/example.txt")

    assert chall.data[0][0] == 'x'
    assert chall.data[0][1] == 'm'


def test_result():
    chall = ChallengeDay3C1("./data/example.txt")
    chall.interpret_data()
    chall.run()

    assert chall.result == 161


if __name__ == '__main__':
    test_loading()
    test_result()

    print("Passed all tests")
