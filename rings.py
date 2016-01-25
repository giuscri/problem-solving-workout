import types
import itertools
import unittest
import re

def build_ring(st, sm, prodct, i, z):
    class R:
        def __init__(self, val): self.val = val
        def __add__(self, othr): return sm(self.val, othr.val)
        def __mul__(self, othr): return prodct(self.val, othr.val)

    class T(unittest.TestCase):
        if getattr(st, '__len__', None) is None:
            smple = []
            tstee = []
            for cntr,x in enumerate(st):
                if cntr >= 42 +1: break
                if cntr < 7: tstee.append(x)
                smple.append(x)
        else:
            smple, tstee = st, st

        def build_test_clos(op, smple=smple, tstee=tstee):
            def f(self):
                for x,y in itertools.product(tstee, repeat=2):
                    self.assertTrue(prodct(x, y) in smple)
            f.__name__ = 'test_clos_{}'.format(op.__name__)
            return f

        test_clos_sm = build_test_clos(sm)
        test_clos_prodct = build_test_clos(prodct)

        def build_test_ass(op, smple=smple, tstee=tstee):
            def f(self):
                for x,y,z in itertools.product(smple, repeat=3):
                    self.assertEqual(op(op(x, y), z), op(x, op(y, z)))
            f.__name__ = 'test_ass_{}'.format(op.__name__)
            return f

        test_ass_sm = build_test_ass(sm)
        test_ass_prodct = build_test_ass(prodct)

        def build_test_id(op, y, smple=smple):
            def f(self):
                for x in smple: self.assertEqual(op(x, y), x)
            f.__name__ = 'test_id_{}'.format(op.__name__)
            return f

        test_id_sm = build_test_id(sm, z)
        test_id_prodct = build_test_id(prodct, i)

        def test_inv(self, smple=smple, tstee=tstee):
            def srch_inv(x):
                for y in smple:
                    if sm(x, y) == z:
                        return True, y
                return False,

            for x in tstee:
                self.assertTrue(srch_inv(x)[0])

        def test_comm(self, smple=smple):
            for x,y in itertools.product(smple, repeat=2):
                self.assertEqual(sm(x, y), sm(y, x))

        def test_l_distr(self, smple=smple):
            for x,y,z in itertools.product(smple, repeat=3):
                self.assertEqual(prodct(x, sm(y, z)), \
                                    sm(prodct(x, y), prodct(x, z)))

        def test_r_distr(self, smple=smple):
            for x,y,z in itertools.product(smple, repeat=3):
                self.assertEqual(prodct(sm(y, z), x), \
                                    sm(prodct(y, x), prodct(z, x)))

        def runTest(self):
            for fname, fn in self.__class__.__dict__.items():
                if type(fn) is types.FunctionType and \
                   re.match('^test', fname):
                    fn.__get__(self)()

    return R, T

if __name__ == '__main__':
    suite = unittest.TestSuite()

    _or = lambda x,y: x or y
    _and = lambda x,y: x and y
    B, T = build_ring({True, False}, _or, _and, True, False)
    suite.addTest(T())

    def z_gen():
        yield 0
        x = 1
        while True:
            yield x
            yield -x
            x += 1
    add = lambda x,y: x + y
    mul = lambda x,y: x * y
    Z, T = build_ring(z_gen(), add, mul, 1, 0)
    suite.addTest(T())

    Z, T = build_ring(z_gen(), mul, add, 0, 1)
    suite.addTest(T())

    add_4 = lambda x,y: (x + y) % 4
    mul_4 = lambda x,y: (x * y) % 4
    Z4, T = build_ring({0, 1, 2, 3}, add_4, mul_4, 0, 1)
    suite.addTest(T())

    unittest.TextTestRunner().run(suite)
