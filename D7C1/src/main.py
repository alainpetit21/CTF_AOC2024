from ChallengeDay7C1 import ChallengeDay7C1


def main():
    chall = ChallengeDay7C1("./data/input.txt")
    chall.interpret_data()

    print(chall.run())


if __name__ == '__main__':
    main()
