from ChallengeDayXCY import ChallengeDayXCY


def main():
    chall = ChallengeDayXCY("./data/input.txt")
    chall.interpret_data()

    print(chall.run())


if __name__ == '__main__':
    main()
