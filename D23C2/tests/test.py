from D23C2.src.ChallengeD23C2 import ChallengeD23C2


def test_loading():
    chall = ChallengeD23C2("./data/example.txt")

    assert chall.data[0][0] == 'k'
    assert chall.data[1][0] == 'q'


def test_connections():
    chall = ChallengeD23C2("./data/example.txt")
    chall.interpret_data()


def test_result():
    chall = ChallengeD23C2("./data/example.txt")
    chall.interpret_data()
    chall.run()
    assert chall.result == "co,de,ka,ta"


if __name__ == '__main__':
    test_loading()
    test_connections()
    test_result()

    print("Passed all tests")
