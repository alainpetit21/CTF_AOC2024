from D2C1.src.ChallengeDay2C1 import ChallengeDay2C1


def test_loading():
    chall = ChallengeDay2C1("./data/example.txt")

    assert chall.data[0][0] == '3'
    assert chall.data[1][0] == '4'


if __name__ == '__main__':
    test_loading()

    print("Passed all tests")
