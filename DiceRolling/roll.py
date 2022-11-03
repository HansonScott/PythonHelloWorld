from Lib.random import randint


def d(sides):
    return randint(1, sides)


def d4():
    return d(4)


def d6():
    return d(6)


def d8():
    return d(8)


def d10():
    return d(10)


def d12():
    return d(12)


def d20():
    return d(20)


def d100():
    return d(100)


def roll_four_d6_less_lowest():
    roll1 = d6()
    roll2 = d6()
    roll3 = d6()
    roll4 = d6()

    rolls = [roll1, roll2, roll3, roll4]
    rolls.sort(reverse=True)

    result = rolls[0] + rolls[1] + rolls[2]

    # print("4d6: " + str(rolls))
    # print("4d6 less lowest: " + str(result))
    return result


def roll_stat_array():
    return [roll_four_d6_less_lowest(),
            roll_four_d6_less_lowest(),
            roll_four_d6_less_lowest(),
            roll_four_d6_less_lowest(),
            roll_four_d6_less_lowest(),
            roll_four_d6_less_lowest()]
