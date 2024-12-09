from D6C2.src.ChallengeDay6C2 import ChallengeDay6C2


def test_loading():
    chall = ChallengeDay6C2("./data/example.txt")

    assert chall.data[0][0] == '.'
    assert chall.data[1][0] == '.'


def interpret_data():
    chall = ChallengeDay6C2("./data/example.txt")
    chall.interpret_data()

    assert chall.guard_pos[0] == 4
    assert chall.guard_pos[1] == 6


def test_new_obstacle_array():
    chall = ChallengeDay6C2("./data/example.txt")
    chall.interpret_data()
    chall.run()

    assert chall.new_obstacle[0] == (3, 6)
    assert chall.new_obstacle[1] == (6, 7)
    assert chall.new_obstacle[2] == (7, 7)
    assert chall.new_obstacle[3] == (1, 8)
    assert chall.new_obstacle[4] == (3, 8)
    assert chall.new_obstacle[5] == (7, 9)


def test_lines():
    chall = ChallengeDay6C2("./data/example.txt")
    lines_m4 = [(4, 6), (4, 5), (4, 4), (4, 3), (4, 2), (4, 1)]
    lines_m3 = [(4, 1), (5, 1), (6, 1), (7, 1), (8, 1)]

    assert chall.lines_are_connected(lines_m4, lines_m3)


def test_path_rectangle():
    lines_m4 = [(4, 6), (4, 5), (4, 4), (4, 3), (4, 2), (4, 1)]
    lines_m3 = [(4, 1), (5, 1), (6, 1), (7, 1), (8, 1)]
    lines_m2 = [(8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6)]
    lines_m1 = [(8, 6), (7, 6), (6, 6), (5, 6), (4, 6)]

    chall = ChallengeDay6C2("./data/example.txt")
    assert chall.is_closed_rectangle(lines_m4, lines_m3, lines_m2, lines_m1)


def test_result():
    chall = ChallengeDay6C2("./data/example.txt")
    chall.interpret_data()
    # chall.run_v1_brute_force_with_lower_seen_spot()
    # assert chall.result == 6

    chall.run()
    assert chall.result == 6


if __name__ == '__main__':
    test_loading()
    test_lines()
    test_path_rectangle()
    test_result()

    print("Passed all tests")
