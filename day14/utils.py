import requests
import pandas as pd
from io import StringIO


def get_data(session, test):
    if test:
        seq = 'NNCB'
        rules = {
            'CH': 'B',
            'HH': 'N',
            'CB': 'H',
            'NH': 'C',
            'HB': 'C',
            'HC': 'B',
            'HN': 'C',
            'NN': 'C',
            'BH': 'H',
            'NC': 'B',
            'NB': 'B',
            'BN': 'B',
            'BB': 'N',
            'BC': 'B',
            'CC': 'N',
            'CN': 'C',
        }
        return seq, rules
    cookies = {
        "session": f"{session}; _ga=GA1.2.1167308080.1638436952; _gid=GA1.2.1150076090.1638436952"
    }
    resp = requests.get("https://adventofcode.com/2021/day/14/input", cookies=cookies)
    df = pd.read_csv(StringIO(resp.content.decode('utf-8')), header=None, sep=' -> ', names=['x', 'y'])
    seq = df[df['y'].isna()].x.values[0]
    rules = df[~df['y'].isna()].set_index('x')['y'].to_dict()
    return seq, rules
