from ChallengeDay6C1 import ChallengeDay6C1


def main():
    chall = ChallengeDay6C1("./data/input.txt")
    chall.interpret_data()

    print(chall.run())


if __name__ == '__main__':
    main()
