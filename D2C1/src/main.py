from ChallengeDay2C1 import ChallengeDay2C1


def main():
    chall = ChallengeDay2C1("./data/input.txt")
    chall.interpret_data()

    print(chall.run())


if __name__ == '__main__':
    main()
