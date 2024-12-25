from D22C1.src.ChallengeD22C1 import ChallengeD22C1
from D22C1.src.RNG import RNG


def test_loading():
    chall = ChallengeD22C1("./data/example.txt")

    assert chall.data[0][0] == '1'
    assert chall.data[1][0] == '1'


def test_interpret_data():
    chall = ChallengeD22C1("./data/example.txt")
    chall.interpret_data()

    assert len(chall.numbers) == 4


def test_mixing_and_pruning():
    chall = ChallengeD22C1("./data/example.txt")
    chall.numbers.append(RNG(42))

    val = chall.numbers[0].mix(chall.numbers[0].get(), 15)
    assert val == 37

    chall.numbers[0] = RNG(100000000)
    val = chall.numbers[0].prune(100000000)
    assert val == 16113920


def test_rng():
    chall = ChallengeD22C1("./data/example.txt")
    chall.numbers.append(RNG(123))

    assert chall.numbers[0].next() == 15887950
    assert chall.numbers[0].next() == 16495136
    assert chall.numbers[0].next() == 527345
    assert chall.numbers[0].next() == 704524
    assert chall.numbers[0].next() == 1553684
    assert chall.numbers[0].next() == 12683156
    assert chall.numbers[0].next() == 11100544
    assert chall.numbers[0].next() == 12249484
    assert chall.numbers[0].next() == 7753432
    assert chall.numbers[0].next() == 5908254


def test_each_serie():
    chall = ChallengeD22C1("./data/example.txt")
    chall.interpret_data()
    chall.run()

    assert chall.numbers[0].get() == 8685429
    assert chall.numbers[1].get() == 4700978
    assert chall.numbers[2].get() == 15273692
    assert chall.numbers[3].get() == 8667524


def test_result():
    chall = ChallengeD22C1("./data/example.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 37327623


if __name__ == '__main__':
    test_loading()
    test_interpret_data()
    test_mixing_and_pruning()
    test_each_serie()
    test_result()

    print("Passed all tests")
