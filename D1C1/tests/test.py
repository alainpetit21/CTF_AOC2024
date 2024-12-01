from D1C1.src.ChallengeDay1C1 import ChallengeDay1C1


def test_loading():
    chall = ChallengeDay1C1("./data/example.txt")

    assert chall.data[0][0] == '3'
    assert chall.data[1][0] == '4'


def test_interpret():
    chall = ChallengeDay1C1("./data/example.txt")
    chall.interpret_data()

    assert chall.list1[0] == 3
    assert chall.list2[0] == 4


def test_sorting():

    chall = ChallengeDay1C1("./data/example.txt")
    chall.interpret_data()
    chall.run()

    assert chall.list1[0] == 1
    assert chall.list2[0] == 3

    assert chall.list1[1] == 2
    assert chall.list2[1] == 3

    assert chall.list1[2] == 3
    assert chall.list2[2] == 3

    assert chall.list1[3] == 3
    assert chall.list2[3] == 4

    assert chall.list1[4] == 3
    assert chall.list2[4] == 5

    assert chall.list1[5] == 4
    assert chall.list2[5] == 9


def test_run():
    chall = ChallengeDay1C1("./data/example.txt")
    chall.interpret_data()
    chall.run()

    assert chall.result == 11


if __name__ == '__main__':
    test_loading()
    test_interpret()
    test_sorting()
    test_run()

    print("Passed all tests")
