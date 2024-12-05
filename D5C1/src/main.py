from ChallengeDay5C1 import ChallengeDay5C1


def main():
    chall = ChallengeDay5C1("./data/input.txt")
    chall.interpret_data()
    chall.load_rule_set()
    chall.load_update_manuals()
    chall.is_manuals_correct()

    print(chall.run())


if __name__ == '__main__':
    main()
