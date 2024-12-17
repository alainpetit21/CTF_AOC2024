from D15C2.src.ChallengeDay15C2 import ChallengeDay15C2


def test_loading():
    chall = ChallengeDay15C2("./data/example.txt")

    assert chall.data[0][0] == '#'
    assert chall.data[1][0] == '#'


def test_interpret_data():
    chall = ChallengeDay15C2("./data/example.txt")
    chall.interpret_data()


def test_result():
    chall = ChallengeDay15C2("./data/example2.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 618

    chall = ChallengeDay15C2("./data/example.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 9021


if __name__ == '__main__':
    test_loading()
    test_interpret_data()
    test_result()

    print("Passed all tests")
