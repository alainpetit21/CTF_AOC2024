from D22C2.src.ChallengeD22C2 import ChallengeD22C2
from D22C2.src.RNG import RNG


def test_loading():
    chall = ChallengeD22C2("./data/example.txt")

    assert chall.data[0][0] == '1'
    assert chall.data[1][0] == '2'


def test_interpret_data():
    chall = ChallengeD22C2("./data/example.txt")
    chall.interpret_data()

    assert len(chall.numbers) == 4


def test_mixing_and_pruning():
    chall = ChallengeD22C2("./data/example.txt")
    chall.numbers.append(RNG(42))

    val = chall.numbers[0].mix(chall.numbers[0].get(), 15)
    assert val == 37

    chall.numbers[0] = RNG(100000000)
    val = chall.numbers[0].prune(100000000)
    assert val == 16113920


def test_all_result():
    chall = ChallengeD22C2("./data/example2.txt", 10)
    chall.interpret_data()
    chall.run()

    assert chall.all_results[0][1] == 15887950
    assert chall.all_results[0][2] == 16495136
    assert chall.all_results[0][3] == 527345
    assert chall.all_results[0][4] == 704524
    assert chall.all_results[0][5] == 1553684
    assert chall.all_results[0][6] == 12683156
    assert chall.all_results[0][7] == 11100544
    assert chall.all_results[0][8] == 12249484
    assert chall.all_results[0][9] == 7753432
    # assert chall.all_results[0][10] == 5908254


def test_mod_10():
    chall = ChallengeD22C2("./data/example2.txt", 10)
    chall.interpret_data()
    chall.run()

    assert chall.all_results_mod_10[0][1] == 0
    assert chall.all_results_mod_10[0][2] == 6
    assert chall.all_results_mod_10[0][3] == 5
    assert chall.all_results_mod_10[0][4] == 4
    assert chall.all_results_mod_10[0][5] == 4
    assert chall.all_results_mod_10[0][6] == 6
    assert chall.all_results_mod_10[0][7] == 4
    assert chall.all_results_mod_10[0][8] == 4
    assert chall.all_results_mod_10[0][9] == 2
    # assert chall.all_results_mod_10[0][10] == 4


def test_deltas():
    chall = ChallengeD22C2("./data/example2.txt", 10)
    chall.interpret_data()
    chall.run()

    assert chall.deltas[0][0] == -3
    assert chall.deltas[0][1] == 6
    assert chall.deltas[0][2] == -1
    assert chall.deltas[0][3] == -1
    assert chall.deltas[0][4] == 0
    assert chall.deltas[0][5] == 2
    assert chall.deltas[0][6] == -2
    assert chall.deltas[0][7] == 0
    assert chall.deltas[0][8] == -2


def test_highest():
    chall = ChallengeD22C2("./data/example.txt")
    chall.interpret_data()
    chall.run()

    assert chall.hh_price == 9

    chall = ChallengeD22C2("./data/example.txt")
    chall.interpret_data()
    chall.run()

    assert chall.hh_price == 9


def test_result():
    chall = ChallengeD22C2("./data/example.txt")
    chall.interpret_data()
    chall.run()

    assert chall.result == 24


def test_sequence_four():
    chall = ChallengeD22C2("./data/example2.txt", 10)
    chall.interpret_data()
    chall.run()

    assert chall.sequence_of_4[0] == -1
    assert chall.sequence_of_4[1] == -1
    assert chall.sequence_of_4[2] == 0
    assert chall.sequence_of_4[3] == 2

    chall = ChallengeD22C2("./data/example.txt")
    chall.interpret_data()
    chall.run()

    assert chall.sequence_of_4[0] == -2
    assert chall.sequence_of_4[1] == 1
    assert chall.sequence_of_4[2] == -1
    assert chall.sequence_of_4[3] == 3


if __name__ == '__main__':
    #test_loading()
    #test_interpret_data()
    #test_mixing_and_pruning()
    #test_all_result()
    #test_mod_10()
    #test_deltas()
    #test_highest()
    # test_sequence_four()
    test_result()

    print("Passed all tests")
