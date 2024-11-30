from D1C1.src.ChallengeDay1C1 import ChallengeDay1C1


def test_loading():
    chall = ChallengeDay1C1("./data/example.txt")

    assert chall.data[0][1] == '3'
    assert chall.data[4][4] == '3'


if __name__ == '__main__':
    test_loading()

    print("Passed all tests")
