class editor:
    def __init__(self):
        self.line = ''
        self.cur = 0

    def x(self):
        if self.cur == 0:
            self.line = self.line[1:]
        elif self.cur == len(self.line) -1:
            self.line = self.line[:-1]
            self.cur -= 1
        else:
            self.line = self.line[:self.cur] + self.line[self.cur +1:]

    def i(self, c):
        if self.line is '':
            self.line = c
        else:
            self.line = self.line[:self.cur +1] + c + self.line[self.cur +1:]
            self.cur += 1

    def l(self, n=1):
        if n + self.cur >= len(self.line):
            self.cur = len(self.line) -1
        else:
            self.cur += n

    def h(self, n=1):
        if self.cur - n < 0:
            self.cur = 0 
        else:
            self.cur -= n

    def dw(self):
        if ' ' in self.line[self.cur:]:
            while self.line[self.cur] != ' ':
                self.x()
        else:
            self.line = self.line[:self.cur]
            if self.cur -1 < 0:
                self.cur = 0
            else:
                self.cur -= 1

    def iw(self, w):
        for c in w: self.i(c)
        self.i(' ')

    def __str__(self):
        return self.line

if __name__ == '__main__':
    ed = editor()
    print(ed)
    ed.x()
    print(ed)
    ed.dw()
    print(ed)
    ed.i('a')
    print(ed)
    ed.x()
    print(ed)
    ed.i('a')
    print(ed)
    ed.i('b')
    print(ed)
    ed.i('c')
    print(ed)
    ed.h()
    ed.dw()
    print(ed)
    ed.iw(" ...")
    print(ed)
    ed.i('z')
    print(ed)
    ed.h(5)
    print(ed)
    ed.x()
    print(ed)
    ed.iw("(Z) ... 1 2 3")
    print(ed)
    ed.iw("Supercalifragilisticexpialidocious")
    print(ed)
    ed.h(len("Supercalifragilisticexpialidocious")+1)
    ed.i('X')
    print(ed)
    ed.l(len("Supercalifragilistic")+1)
    print(ed)
    ed.dw()
    print(ed)
