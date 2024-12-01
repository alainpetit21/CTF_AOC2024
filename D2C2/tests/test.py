from D2C2.src.ChallengeDay2C2 import ChallengeDay2C2


def test_loading():
    chall = ChallengeDay2C2("./data/example.txt")

    assert chall.data[0][0] == '3'
    assert chall.data[1][0] == '4'


if __name__ == '__main__':
    test_loading()

    print("Passed all tests")
