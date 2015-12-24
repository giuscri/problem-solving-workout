import re

class calculator:
    def __init__(self, pfix):
        self.pfix = pfix

        self.r_pfix = ''.join(reversed(self.pfix))
        self.lst = []
        self.ifix = ''

        for c in self.r_pfix:
            if c in {'+', '-', '*', '/'}:
                assert len(self.lst) >= 2
                x = self.lst.pop()
                y = self.lst.pop()
                z = '({} {} {})'.format(x, c, y)
                self.lst.append(z)
            else:
                self.lst.append(c)

        self.ifix = self.lst.pop()
        assert len(self.lst) == 0

    def __str__(self):
        return self.ifix

def print_reduction(c):

    ifix = str(c)
    
    print(ifix)

    r = re.compile('\([0-9]+ [\+\-\*/] [\-]{,1}[0-9]+\)')
    while r.search(ifix) is not None:
        nmatches = len(r.findall(ifix))

        for i in range(nmatches):
            m = r.search(ifix)

            evald = eval(ifix[m.start():m.end()])
            if type(evald) is float: evald = int(evald)

            ifix = [
                ifix[:m.start()],
                str(evald),
                ifix[m.end():],
            ]
            ifix = ''.join(ifix)

        print(ifix)

    if r.search(ifix) is not None: print(eval(ifix))

if __name__ == '__main__':
    expressions = ["+34", "+3-15", "*+34-23", "+7++34+23",
    "*+*34-34/6-35", "/+-81*45*/93/52", "*+/12/14-2/32", "+2*-53/63"]
    [print_reduction(calculator(expr)) for expr in expressions]
