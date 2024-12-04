from ChallengeDay4C1 import ChallengeDay4C1


def main():
    chall = ChallengeDay4C1("./data/input.txt")
    chall.interpret_data()

    print(chall.run())


if __name__ == '__main__':
    main()
