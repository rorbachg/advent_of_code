from collections import Counter
from utils import get_data


def get_substr(seq):
    counter = 0
    while counter < len(seq)-1:
        yield seq[counter:counter+2]
        counter += 1


def polimeriation_step(rules, cnt_m, cnt_d):
    new_cnt_d = cnt_d.copy()
    for pair, value in cnt_d.items():
        if middle := rules.get(pair):
            new_cnt_d[pair[0] + middle] += value
            new_cnt_d[middle + pair[1]] += value
            new_cnt_d[pair] -= value
            cnt_m[middle] += value
    return cnt_m, new_cnt_d


def main(seq, rules, days):
    cnt_d = Counter(get_substr(seq))
    cnt_m = Counter(seq)
    for _ in range(days):
        cnt_m, cnt_d = polimeriation_step(rules, cnt_m, cnt_d)

    print(cnt_d)
    print(cnt_m.most_common()[0][1] - cnt_m.most_common()[-1][1])


if __name__ == '__main__':
    session = "53616c7465645f5ff7db31f30dbc39e8efa073d984f1019c423857460dd4104435d33265120f00431aafacd6a212e84f"
    seq, rules = get_data(session, test=False)
    days = 40

    main(seq, rules, days)
