import random
import pandas as pd


def get_chain_data(year):
    raw = open_santa_data(year)
    return {
        'emails': open_emails_data(year),
        'chain': generate_chain(raw)
    }


def open_emails_data(year):
    output_dict = {}
    filename = f'data/{year}_emails.csv'
    df = pd.read_csv(filename)
    for record in df.to_dict('records'):
        output_dict[record['Name']] = record['Email']
    return output_dict


def open_santa_data(year):
    output_dict = {}
    filename = f'data/{year}.csv'
    df = pd.read_csv(filename)
    for record in df.to_dict('records'):
        source = record['source']
        output_dict[source] = output_dict.get(source, []) + [record['target']]
    return output_dict


def generate_chain(data):
    chosen_targets = set()
    output_chain = {}
    l = []
    for key in data:
        l.append((key, data[key]))
    l.sort(key=lambda x: len(x[1]))
    for key_data_pair in l:
        source = key_data_pair[0]
        choices = list(filter(lambda x: x not in chosen_targets, key_data_pair[1]))
        if choices:
            target = random.choice(choices)
            output_chain[source] = target
            chosen_targets.add(target)
        else:
            print('Failed chain, trying again...')
            return generate_chain(data)
    return output_chain


if __name__ == '__main__':
    d = get_chain_data(2021)
    print()
