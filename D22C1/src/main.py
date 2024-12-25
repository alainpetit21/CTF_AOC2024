from ChallengeD22C1 import ChallengeD22C1


def main():
    chall = ChallengeD22C1("./data/input.txt")
    chall.interpret_data()

    print(chall.run())


if __name__ == '__main__':
    main()
