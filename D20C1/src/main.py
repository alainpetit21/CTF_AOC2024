from ChallengeD20C1 import ChallengeD20C1


def main():
    chall = ChallengeD20C1("./data/input.txt")
    chall.interpret_data()

    print(chall.run())


if __name__ == '__main__':
    main()
