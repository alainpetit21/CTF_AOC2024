from D1C2.src.ChallengeDay1C2 import ChallengeDay1C2


def test_loading():
    chall = ChallengeDay1C2("./data/example.txt")

    assert chall.data[0][0] == '3'
    assert chall.data[1][0] == '4'


def test_interpret():
    chall = ChallengeDay1C2("./data/example.txt")
    chall.interpret_data()

    assert chall.list1[0] == 3
    assert chall.list2[0] == 4


def test_multiplications():

    chall = ChallengeDay1C2("./data/example.txt")
    chall.interpret_data()
    chall.run()

    assert chall.muls[0] == 9
    assert chall.muls[1] == 4
    assert chall.muls[2] == 0
    assert chall.muls[3] == 0
    assert chall.muls[4] == 9
    assert chall.muls[5] == 9


def test_run():
    chall = ChallengeDay1C2("./data/example.txt")
    chall.interpret_data()
    chall.run()

    assert chall.result == 31


if __name__ == '__main__':
    test_loading()
    test_interpret()
    test_multiplications()
    test_run()

    print("Passed all tests")
