from D11C2.src.ChallengeDay11C2 import ChallengeDay11C2


def test_loading():
    chall = ChallengeDay11C2("./data/example.txt")

    assert chall.data[0][0] == '0'
    assert chall.data[0][1] == ' '


def test_interpret_data():
    chall = ChallengeDay11C2("./data/example.txt")
    chall.interpret_data()

    assert len(chall.stone_counts) == 5


def test_result():
    chall = ChallengeDay11C2("./data/example.txt", 1)
    chall.interpret_data()
    chall.run()
    assert chall.result == 7

    chall = ChallengeDay11C2("./data/example2.txt", 6)
    chall.interpret_data()
    chall.run()
    assert chall.result == 22

    chall = ChallengeDay11C2("./data/example2.txt", 25)
    chall.interpret_data()
    chall.run()
    assert chall.result == 55312


if __name__ == '__main__':
    test_loading()
    test_interpret_data()
    test_result()

    print("Passed all tests")
