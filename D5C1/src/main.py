from ChallengeDay5C1 import ChallengeDay5C1


def main():
    chall = ChallengeDay5C1("./data/input.txt")
    chall.interpret_data()

    print(chall.run())


if __name__ == '__main__':
    main()
