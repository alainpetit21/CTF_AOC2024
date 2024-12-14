from D11C1.src.ChallengeDay11C1 import ChallengeDay11C1


def test_loading():
    chall = ChallengeDay11C1("./data/example.txt")

    assert chall.data[0][0] == '8'
    assert chall.data[1][0] == '7'


def test_interpret_data():
    chall = ChallengeDay11C1("./data/example.txt")
    chall.interpret_data()


def test_result():
    chall = ChallengeDay11C1("./data/example1.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 2

    chall = ChallengeDay11C1("./data/example2.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 4

    chall = ChallengeDay11C1("./data/example3.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 3

    chall = ChallengeDay11C1("./data/example.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 36


if __name__ == '__main__':
    test_loading()
    test_interpret_data()
    test_result()

    print("Passed all tests")
