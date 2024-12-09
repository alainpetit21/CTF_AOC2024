from D9C1.src.ChallengeDay9C1 import ChallengeDay9C1


def test_loading():
    chall = ChallengeDay9C1("./data/example.txt")

    assert chall.data[0][0] == '2'
    assert chall.data[0][1] == '3'


def interpret_data():
    chall = ChallengeDay9C1("./data/example.txt")
    chall.interpret_data()


def test_decode():
    chall = ChallengeDay9C1("./data/example.txt")
    chall.interpret_data()
    chall.decode_input()

    assert chall.decoded == [0, 0, '.', '.', '.', 1, 1, 1, '.', '.', '.', 2, '.', '.', '.', 3, 3, 3, '.', 4, 4, '.', 5, 5, 5, 5, '.', 6, 6, 6, 6, '.', 7, 7, 7, '.', 8, 8, 8, 8, 9, 9]


def test_compress_filesystem():
    chall = ChallengeDay9C1("./data/example.txt")
    chall.interpret_data()
    chall.decode_input()
    chall.compress_filesystem()

    temp = [int(val) for val in "0099811188827773336446555566"]

    for i in range(len("..............")):
        temp.append('.')

    assert chall.newData == temp


def test_result():
    chall = ChallengeDay9C1("./data/example.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 1928


if __name__ == '__main__':
    test_loading()
    test_decode()
    test_compress_filesystem()
    test_result()

    print("Passed all tests")
