from ChallengeDay1C1 import ChallengeDay1C1


def main():
    chall = ChallengeDay1C1("./data/input.txt")
    chall.interpret_data()

    print(chall.run())


if __name__ == '__main__':
    main()
