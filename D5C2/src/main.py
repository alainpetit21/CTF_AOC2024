from ChallengeDay5C2 import ChallengeDay5C2


def main():
    chall = ChallengeDay5C2("./data/input.txt")
    chall.interpret_data()

    print(chall.run())


if __name__ == '__main__':
    main()
