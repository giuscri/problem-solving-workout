import itertools

def f0(g):
    return len(list(filter(lambda x: x=='red', \
                              map(lambda t: t[1], g)))) == 1

def f1(g):
    fred_pos = list(filter(lambda t: t[0]=='fred', g))[0][-1]
    lst = list(filter(lambda t: t[-1]==fred_pos+1, g))
    return len(lst) > 0 and lst[0][1] == 'blue'

def f2(g):
    return list(filter(lambda t: t[0]=='joe', g))[0][-1] == 2

def f3(g):
    return list(filter(lambda t: t[0]=='bob', g))[0][1] == 'plaid'

def f4(g):
    tom = list(filter(lambda t: t[0]=='tom', g))[0]
    return tom[-1] != 1 and tom[-1] != 4 and tom[1] != 'orange'
    

rules = (
    f0,
    f1,
    f2,
    f3,
    f4,
)

class Drools:
    def __init__(self, rules, *lsts):
        self.rules = rules
        self.lsts = lsts

    def eval(self):
        def valid_group(g, seen=[]):
            if len(g) == 0: return True
            for x in g[0]:
                if x in seen: return False
            return valid_group(g[1:], seen + list(g[0]))

        gs = filter(valid_group, \
               itertools.combinations( \
                  itertools.product(*self.lsts), len(self.lsts[0])))

        ok_gs = []
        for g in gs:
            ok = True

            for r in rules:
                if not r(g):
                    ok = False

            if ok: ok_gs.append(g)

        fmt = 'Golfer {} is in position {} and wears some {} pants.'
        for g in ok_gs:
            for glf in g:
                print(fmt.format(glf[0], glf[-1], glf[1]))
            print('------------------------------------------------------')

if __name__ == "__main__":
    d = Drools(rules,
    ['bob', 'joe', 'fred', 'tom'],
    ['red', 'orange', 'blue', 'plaid'],list(range(1,5)))

    d.eval()
