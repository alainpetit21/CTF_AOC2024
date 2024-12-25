from D23C1.src.ChallengeD23C1 import ChallengeD23C1


def test_loading():
    chall = ChallengeD23C1("./data/example.txt")

    assert chall.data[0][0] == 'k'
    assert chall.data[1][0] == 'q'


def test_connections():
    chall = ChallengeD23C1("./data/example.txt")
    chall.interpret_data()
    chall.build_connection_of_3()

    assert len(chall.connections3) == 12


def test_result():
    chall = ChallengeD23C1("./data/example.txt")
    chall.interpret_data()
    chall.run()
    assert chall.result == 7


if __name__ == '__main__':
    test_loading()
    test_connections()
    test_result()

    print("Passed all tests")
