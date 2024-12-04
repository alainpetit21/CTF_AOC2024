from D2C2.src.ChallengeDay2C2 import ChallengeDay3C1


def test_loading():
    chall = ChallengeDay3C1("./data/example.txt")

    assert chall.data[0][0] == '7'
    assert chall.data[1][0] == '1'


def test_report_num():
    chall = ChallengeDay3C1("./data/example.txt")
    chall.interpret_data()

    assert chall.data_num[0][0] == 7
    assert chall.data_num[5][4] == 9


def test_result():
    chall = ChallengeDay3C1("./data/example.txt")
    chall.interpret_data()
    chall.run()

    assert chall.result == 4


if __name__ == '__main__':
    test_loading()
    test_report_num()
    test_result()

    print("Passed all tests")
