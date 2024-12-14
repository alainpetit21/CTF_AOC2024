from D11C2.src.ChallengeDay11C2 import ChallengeDay11C2


def test_loading():
    chall = ChallengeDay11C2("./data/example.txt")

    assert chall.data[0][0] == '8'
    assert chall.data[1][0] == '7'


def test_interpret_data():
    chall = ChallengeDay11C2("./data/example.txt")
    chall.interpret_data()


def test_result():
    chall = ChallengeDay11C2("./data/example.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 2


if __name__ == '__main__':
    test_loading()
    test_interpret_data()
    test_result()

    print("Passed all tests")
