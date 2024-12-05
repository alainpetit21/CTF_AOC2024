from D5C1.src.ChallengeDay5C1 import ChallengeDay5C1


def test_loading():
    chall = ChallengeDay5C1("./data/example.txt")

    assert chall.data[0][0] == '4'
    assert chall.data[1][0] == '9'


def test_load_rules():
    chall = ChallengeDay5C1("./data/example.txt")
    chall.interpret_data()
    chall.load_rule_set()

    assert chall.rules[0][0] == 47
    assert chall.rules[0][1] == 53
    assert chall.rules[20][0] == 53
    assert chall.rules[20][1] == 13
    assert chall.start_manual_line == 22


def test_load_manuals():
    chall = ChallengeDay5C1("./data/example.txt")
    chall.interpret_data()
    chall.load_rule_set()
    chall.load_update_manuals()

    assert len(chall.manuals) == 6

    assert chall.manuals[0][0] == 75
    assert chall.manuals[1][0] == 97
    assert chall.manuals[2][0] == 75
    assert chall.manuals[3][0] == 75
    assert chall.manuals[4][0] == 61
    assert chall.manuals[5][0] == 97


def test_correct_manual():
    chall = ChallengeDay5C1("./data/example.txt")
    chall.interpret_data()
    chall.load_rule_set()
    chall.load_update_manuals()
    chall.is_manuals_correct()
    chall.run()

    assert chall.is_correct[0]
    assert chall.is_correct[1]
    assert chall.is_correct[2]
    assert not chall.is_correct[3]
    assert not chall.is_correct[4]


def test_result():
    chall = ChallengeDay5C1("./data/example.txt")
    chall.interpret_data()
    chall.load_rule_set()
    chall.load_update_manuals()
    chall.is_manuals_correct()
    chall.run()

    assert chall.result == 143


if __name__ == '__main__':
    test_loading()
    test_load_rules()
    test_load_manuals()
    test_correct_manual()
    test_result()

    print("Passed all tests")
