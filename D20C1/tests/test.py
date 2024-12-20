from D20C1.src.ChallengeD20C1 import ChallengeD20C1


def test_loading():
    chall = ChallengeD20C1("./data/example.txt")

    assert chall.data[0][0] == '#'
    assert chall.data[1][0] == '#'


def test_interpret_data():
    chall = ChallengeD20C1("./data/example.txt")
    chall.interpret_data()

    assert chall.tilemap[0][0].is_wall
    assert chall.start == (1, 3)
    assert chall.goal == (5, 7)

    assert chall.width_tiles == 15
    assert chall.height_tiles == 15


def test_result():
    chall = ChallengeD20C1("./data/example.txt")
    chall.interpret_data()
    chall.run()
    assert chall.result == 0

    assert len(chall.cheats) == 44


if __name__ == '__main__':
    test_loading()
    test_interpret_data()
    test_result()

    print("Passed all tests")
