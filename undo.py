class editor:
    def __init__(self):
        self.line = ''
        self.cur = 0

    def l(self, n=1):
        self._cur = self.cur
        if n + self.cur >= len(self.line):
            self.cur = len(self.line) -1
        else:
            self.cur += n
        return self.cur - self._cur

    def h(self, n=1):
        self._cur = self.cur
        if self.cur - n < 0:
            self.cur = 0 
        else:
            self.cur -= n
        return self.cur - self._cur

    def i(self, c):
        if self.line is '':
            self.line = c
        else:
            self.line = self.line[:self.cur +1] + c + self.line[self.cur +1:]
            self.cur += 1

    def iw(self, w):
        if self.cur == 0: pass
        else: self.cur += 1
        self.line = self.line[:self.cur] + w+' ' + self.line[self.cur:]
        self.cur += len(w)

    def x(self):
        if self.cur == 0:
            self.line = self.line[1:]
        elif self.cur == len(self.line) -1:
            self.line = self.line[:-1]
            self.cur -= 1
        else:
            self.line = self.line[:self.cur] + self.line[self.cur +1:]
        return ret

    def dw(self):
        if ' ' in self.line[self.cur:]:
            ret = ''
            i = self.cur
            j = i
            while self.line[j] != ' ':
                ret += self.line[j]
                j += 1
            ret += ' '
            self.line = self.line[:i] + self.line[j+1:]
        else:
            self.line = self.line[:self.cur]
            ret = self.line[self.cur:]
            if self.cur -1 < 0:
                self.cur = 0
            else:
                self.cur -= 1
        return ret

    def __str__(self):
        return self.line

class meta_editor(type):
    def __new__(meta, name, supers, clsdict):
        import types
        def dec(f):
            def _f(self, *args, **kwargs):
                msg = {}
                msg['retnd_value'] = f.__get__(self)(*args, **kwargs)
                msg['method'] = f.__name__
                if getattr(self, '_undo_cache', None) is None:
                    self._undo_cache = [msg]
                else:
                    self._undo_cache.append(msg)
                return msg['retnd_value']
            return _f

        origs = dict()
        for k,v in clsdict.items():
            if type(v) is types.FunctionType \
               and v.__name__ not in ['__init__', '__str__']:
                origs['_'+k] = clsdict[k]
                clsdict[k] = dec(clsdict[k])
        clsdict.update(origs)

        def __apply_msg(ed, msg):
            if msg['method'] in ['l', 'h']:
                getattr(ed, ''.join(['_',msg['method']]))(msg['parameter'])
        clsdict['__apply_msg'] = __apply_msg

        def __invert_msg(msg):
            _msg = {}
            if msg['method'] == 'l':
                _msg['method'] = 'h'
                _msg['parameter'] = -1*msg['retnd_value']
                return _msg
            elif msg['method'] == 'h':
                _msg['method'] = 'l'
                _msg['parameter'] = -1*msg['retnd_value']
                return _msg
        clsdict['__invert_msg'] = __invert_msg

        def undo(self):
            if getattr(self, '_undo_cache', None) is None: return
            if len(self._undo_cache) == 0: return

            ppd = self._undo_cache.pop()
            inv_ppd = __invert_msg(ppd)
            if getattr(self, '_ctrlr_cache', None) is None:
                self._ctrlr_cache = [inv_ppd]
            else:
                self._ctrlr_cache.append(inv_ppd)

            __apply_msg(self, inv_ppd)
        clsdict['undo'] = undo

        def ctrlr(self):
            if getattr(self, '_ctrlr_cache', None) is None: return
            if len(self._ctrlr_cache) == 0: return

            ppd = self._ctrlr_cache.pop()
            inv_ppd = __invert_msg(ppd)

            getattr(self, inv_ppd[0])(inv_ppd[1])
        clsdict['ctrlr'] = ctrlr

        return type.__new__(meta, name, supers, clsdict)

editor = meta_editor('editor', (), dict(editor.__dict__))

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
