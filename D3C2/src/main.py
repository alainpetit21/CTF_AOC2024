from ChallengeDay3C2 import ChallengeDay3C2


def main():
    chall = ChallengeDay3C2("./data/input.txt")
    chall.interpret_data()

    print(chall.run())


if __name__ == '__main__':
    main()
