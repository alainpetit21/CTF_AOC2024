from ChallengeDay3C1 import ChallengeDay3C1


def main():
    chall = ChallengeDay3C1("./data/input.txt")
    chall.interpret_data()

    print(chall.run())


if __name__ == '__main__':
    main()
