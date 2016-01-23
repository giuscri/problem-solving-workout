from ruzzle import ruzzles
import unittest
import functools

def valid_chain(c):
    for i in range(len(c) -1):
        x, y = c[i], c[i + 1]
        if x[0] == y[0]:
            if x[1] != y[1] +1 and x[1] != y[1] -1:
                return False
        elif x[1] == y[1]:
            if x[0] != y[0] +1 and x[0] != y[0] -1:
                return False
        else:
            return False
    return True

def build_chains(w, g):
    def f(s, cn, cns):
        if len(s) == 0:
            return cns.append(cn) or cns
        for i in range(len(g)):
            for j in range(len(g[0])):
                if g[i][j] == s[0]:
                    f(s[1:], cn + [(i,j)], cns)
        return cns
    return f(w, [], [])

class test_ruzzles(unittest.TestCase):
    grds = (
        ["abst", "oime", "uesl", "snsp"],
        ["essx", "ndet", "sigh", "raen"],
        ["poap", "lkjh", "aswe", "jhnh"],
    )

    def test_sorted_res(self, grds=grds):
        for g in grds:
            res = ruzzles(g)
            self.assertEqual(res, sorted(res))

    def test_english_words(self, grds=grds):
        with open('wordlist.txt', 'r') as f:
            ws = f.read().strip().split()
        for g in grds:
            res = ruzzles(g)
            for w in res:
                self.assertTrue(w in ws)

    def test_len_words(self, grds=grds):
        for g in grds:
            res = ruzzles(g)
            for w in res:
                self.assertTrue(len(w) in range(3, len(g)*len(g[0]) +1))

    def test_char_times_words(self, grds=grds):
        for g in grds:
            res = ruzzles(g)
            for w in res:
                for c in set(w):
                    self.assertTrue(w.count(c) <= ''.join(g).count(c))

    def test_hidden_words(self, grds=grds):
        for g in grds:
            res = ruzzles(g)
            for w in res:
                cns = build_chains(w, g)
                at_least_one = \
                   functools.reduce(lambda x,y: x or y, \
                                       map(valid_chain, cns))
                self.assertTrue(at_least_one, (cns, w, g))

if __name__ == '__main__':
    unittest.main()
