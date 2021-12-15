from collections import Counter
from utils import get_data


def get_substr(seq):
    counter = 0
    while counter < len(seq)-1:
        yield seq[counter:counter+2]
        counter += 1


def pair_insertion(pair, rules):
    return pair[0] + rules.get(pair, '') + pair[1]


def polimeriation_step(seq, rules):
    new_seq = ''
    for i in get_substr(seq):
        if len(new_seq):
            new_seq = new_seq[:-1]
        new_seq += pair_insertion(i, rules)
    return new_seq


def main(seq, rules, days):
    for _ in range(days):
        seq = polimeriation_step(seq, rules)
    cnt = Counter(seq)
    print(seq)
    print(cnt.most_common()[0][1] - cnt.most_common()[-1][1])


if __name__ == '__main__':
    session = "53616c7465645f5ff7db31f30dbc39e8efa073d984f1019c423857460dd4104435d33265120f00431aafacd6a212e84f"
    seq, rules = get_data(session, test=False)
    days = 10

    main(seq, rules, days)
