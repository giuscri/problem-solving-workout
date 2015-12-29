class calculator:
    def __init__(self, expression):
        self.expression = expression

        def f(expr, stk=[], insts=[]):
            def add(a,b): return a+b
            def sub(a,b): return a-b
            def mul(a,b): return a*b
            def div(a,b): return a//b

            ops = { '+': add, '-': sub, '*': mul, '/': div }

            if len(expr)==0:
                return stk.pop(), insts.pop()

            if expr[0] in {'+', '-', '*', '/'}:
                a,b = stk.pop(),stk.pop()
                stk.append(ops[expr[0]](a, b))

                x,y = insts.pop(), insts.pop()
                insts.append('{}{}{}\n'.format( \
                                x, y, ops[expr[0]].__name__))
            else:
                stk.append(int(expr[0]))

                insts.append('store {}\n'.format(expr[0]))
            return f(expr[1:], stk, insts)

        self.evald, self.insts = f(''.join(list(reversed(list(expression)))))

    def eval(self): return self.evald

    def code(self): return self.insts

if __name__ == '__main__':
    print("### test +2*-53/63")
    calc = calculator('+2*-53/63') # ((6/3)*(5-3))+2
    print(calc.eval())
    print(calc.code(),end='')
