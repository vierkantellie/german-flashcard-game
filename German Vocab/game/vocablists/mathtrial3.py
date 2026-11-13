def a(choices):
    randval = 4
    for choice, weight in choices:
        if randval <= weight:
            return choice
        else:
            randval -= weight


def b():
    weights = [("yellowList", 70), ("redList", 25), ("greenList", 5)]
    randval = 4
    for choice, weight in weights:
        if randval <= weight:
            winner = choice
        else:
            randval -= weight
    return winner
