from D12C2.src.ChallengeDay12C2 import ChallengeDay12C2


def test_loading():
    chall = ChallengeDay12C2("./data/example.txt")

    assert chall.data[0][0] == 'A'
    assert chall.data[1][0] == 'B'


def test_interpret_data():
    chall = ChallengeDay12C2("./data/example.txt")
    chall.interpret_data()


def test_result():
    chall = ChallengeDay12C2("./data/example.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 80

    chall = ChallengeDay12C2("./data/example2.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 236

    chall = ChallengeDay12C2("./data/example3.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 368

    chall = ChallengeDay12C2("./data/example4.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 1206


if __name__ == '__main__':
    test_loading()
    test_interpret_data()
    test_result()

    print("Passed all tests")
