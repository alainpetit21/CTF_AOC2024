from D5C2.src.ChallengeDay5C2 import ChallengeDay5C2


def test_loading():
    chall = ChallengeDay5C2("./data/example.txt")

    assert chall.data[0][0] == '.'
    assert chall.data[1][0] == '.'


def test_result():
    chall = ChallengeDay5C2("./data/example.txt")
    chall.interpret_data()
    chall.run()

    assert chall.result == 9


if __name__ == '__main__':
    test_loading()
    test_result()

    print("Passed all tests")
