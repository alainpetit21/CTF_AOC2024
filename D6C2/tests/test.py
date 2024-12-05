from D6C2.src.ChallengeDay6C2 import ChallengeDay6C2


def test_loading():
    chall = ChallengeDay6C2("./data/example.txt")

    assert chall.data[0][0] == '4'
    assert chall.data[1][0] == '9'


def test_result():
    chall = ChallengeDay6C2("./data/example.txt")
    chall.interpret_data()
    chall.run()

    assert chall.result == 123


if __name__ == '__main__':
    test_loading()
    test_result()

    print("Passed all tests")
