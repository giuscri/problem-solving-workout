import re

def reverse_tuple(tple):
    ret = []
    smple_syn, hard_ws = tple[0], tple[1]
    for w in hard_ws: ret.append((w, smple_syn))
    return ret

def build_dictionary(fname='synonyms-list.txt'):
    d = []
    with open(fname) as f: lns = f.read().strip().split('\n')
    for l in lns:
        _lst = list(map(lambda x: x.strip(), re.split(':', l)))
        assert len(_lst) == 2
        smple = _lst[0]
        cmpls = re.split('\W+', _lst[1])
        tple = (smple, cmpls)
        d.extend(reverse_tuple(tple))
    return dict(d)

d = build_dictionary()

def replace_synonyms(s, d=d):
    ws = re.split('\s+', s)
    return ' '.join(map(lambda w, d=d: w in d and d[w].upper() or w, ws))

if __name__ == "__main__":
    s0 = "The deadline is approximately midnight though it could vary."
    s1 = "She is a fascinating lady; she has an astonishing smile, an alluring voice and an entertaining sense of humor."
    s2 = "The topic is appealing nevertheless the speaker was too monotonous."
    print(replace_synonyms(s0))
    print(replace_synonyms(s1))
    print(replace_synonyms(s2))
