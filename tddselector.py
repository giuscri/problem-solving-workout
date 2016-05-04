import types
import unittest

def SelectorPresenceTest(cls, obj):
    class C(unittest.TestCase):
        def test_getters(self, cls=cls, obj=obj):
            for k,v in obj.__dict__.items():
                if type(v) is not types.FunctionType:
                    name = 'get{}'.format(k)
                    self.assertTrue(getattr(obj, name, None) is not None)

        def test_setters(self, cls=cls, obj=obj):
            for k,v in obj.__dict__.items():
                if type(v) is not types.FunctionType:
                    name = 'set{}'.format(k)
                    self.assertTrue(getattr(obj, name, None) is not None)
    return C

class TestClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = 0
    def getx(self): return x
    def getz(self): return z
    def setz(self, x): self.z = x

class TestClass2(TestClass):
    def sety(self, z): self.y=z
    def gety(self): return self.y

ClassesToTest = [
    SelectorPresenceTest(TestClass, TestClass(7,25)),
    SelectorPresenceTest(TestClass2, TestClass2(7,25))
]

if __name__ == "__main__":
    suite = unittest.TestSuite()
    for tc in ClassesToTest:
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(tc))
    unittest.TextTestRunner(verbosity=2).run(suite)
