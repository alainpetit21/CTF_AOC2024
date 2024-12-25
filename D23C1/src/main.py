from ChallengeD23C1 import ChallengeD23C1


def main():
    chall = ChallengeD23C1("./data/input.txt")
    chall.interpret_data()

    print(chall.run())


if __name__ == '__main__':
    main()
