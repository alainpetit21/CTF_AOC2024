from D2C1.src.ChallengeDay2C1 import ChallengeDay2C1


def test_loading():
    chall = ChallengeDay2C1("./data/example.txt")

    assert chall.data[0][0] == '7'
    assert chall.data[1][0] == '1'


def test_report_num():
    chall = ChallengeDay2C1("./data/example.txt")
    chall.interpret_data()

    assert chall.data_num[0][0] == 7
    assert chall.data_num[5][4] == 9


def test_dec_or_inc():
    chall = ChallengeDay2C1("./data/example.txt")
    chall.interpret_data()
    chall.run()

    assert chall.report_is_inc[0] == False
    assert chall.report_is_inc[1] == True
    assert chall.report_is_inc[2] == False
    assert chall.report_is_inc[3] == True
    assert chall.report_is_inc[4] == False
    assert chall.report_is_inc[5] == True


def test_result():
    chall = ChallengeDay2C1("./data/example.txt")
    chall.interpret_data()
    chall.run()

    assert chall.result == 2


if __name__ == '__main__':
    test_loading()
    test_report_num()
    test_dec_or_inc()
    test_result()

    print("Passed all tests")
