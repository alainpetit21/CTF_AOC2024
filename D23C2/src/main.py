from ChallengeD23C2 import ChallengeD23C2


def main():
    chall = ChallengeD23C2("./data/input.txt")
    chall.interpret_data()

    print(chall.run())


if __name__ == '__main__':
    main()
