import re

def build_noun_lst(fname='nounlist.txt'):
    with open(fname, 'r') as f:
        ret = list(map(lambda w: w.lower(), \
                          f.read().strip().split()))
    return ret

noun_lst = build_noun_lst()

def tags(fname, noun_lst=noun_lst):
    d = dict()
    with open(fname, 'r') as f:
        ws = re.split('\W+', f.read().strip())
    ws = list(map(lambda w: w.lower(), ws))
    for w in ws:
        if w in d:
            d[w] += 1
        elif w in noun_lst:
            d[w] = 1
    ret = list(d.items())
    return ret.sort(key=lambda p: p[1],reverse=True) or ret
