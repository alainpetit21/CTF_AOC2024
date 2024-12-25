from ChallengeD22C2 import ChallengeD22C2


def main():
    chall = ChallengeD22C2("./data/input.txt")
    chall.interpret_data()

    print(chall.run())


if __name__ == '__main__':
    main()
