from ChallengeDay2C2 import ChallengeDay2C2


def main():
    chall = ChallengeDay2C2("./data/input.txt")
    chall.interpret_data()

    print(chall.run())


if __name__ == '__main__':
    main()
