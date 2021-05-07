def latest(scores):
    # returns the last {object} from the {argument} if the passed argument is a list
    # equivalent to 'scores{len(scores) + 1'

    return scores[-1]


def personal_best(scores):
    # returns the maximum {object} value, independent of quantity, from the {argument} if the passed argument is a list

    return max(scores)


def personal_top_three(scores):
    # returns a list of the last three maximum {objects} if the passed argument is a list starting from
    # the returned list is arranged from largest to least

    return sorted(scores, reverse=True)[:3]
