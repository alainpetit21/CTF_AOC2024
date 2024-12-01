from ChallengeDay1C2 import ChallengeDay1C2


def main():
    chall = ChallengeDay1C2("./data/input.txt")
    chall.interpret_data()

    print(chall.run())


if __name__ == '__main__':
    main()
