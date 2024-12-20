from ChallengeD19C1 import ChallengeD19C1


def main():
    chall = ChallengeD19C1("./data/input.txt")
    chall.interpret_data()

    print(chall.run())


if __name__ == '__main__':
    main()
