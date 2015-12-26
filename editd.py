def chain(source, target):
    ls = [chr(x) for x in range(ord('a'), ord('z') + 1)]

    with open('dict.txt', 'r') as f:
        d = f.read().strip().split('\n')

    def _chain(source, target, cn, cns=[]):
        if source==target:
            return cns.append(cn)

        ws = set()
        for i in range(len(source)):
            lst = [source[:i] + l + source[i+1:] \
                      for l in ls]
            lst = filter(lambda x,source=source: x in d and x not in cn, lst)
            ws.update(list(set(lst)))

        for w in ws:
            if w in cn: continue

            _chain(w, target, cn + [w], cns)

        return cns

    return _chain(source, target, [source])
