from ChallengeD20C2 import ChallengeD20C2


def main():
    chall = ChallengeD20C2("./data/input.txt")
    chall.interpret_data()

    print(chall.run())


if __name__ == '__main__':
    main()
