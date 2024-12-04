from ChallengeDay4C2 import ChallengeDay4C2


def main():
    chall = ChallengeDay4C2("./data/input.txt")
    chall.interpret_data()

    print(chall.run())


if __name__ == '__main__':
    main()
