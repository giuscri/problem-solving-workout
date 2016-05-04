import re

def prettyCSV(fname):

    with open(fname, 'r') as f:
        recs = f.read().strip().split('\n')

    hdr, recs = recs[0], recs[1:]

    hdr = list(map(lambda s: s.strip(), re.split(';', hdr)))

    recs = map(lambda r: re.split(';', r), recs)
    recs = map(lambda r: list(map(lambda s: s.strip(), r)), recs)
    recs = list(recs)

    def f(spans, i=0):
        if i == len(hdr):
            return spans

        def _f(lst, span, spans):
            if len(lst) == 0:
                return spans.append(span) or spans
            if len(lst[0][i]) > span:
                span = len(lst[0][i])
            return _f(lst[1:], span, spans)
        _f(recs, len(hdr[i]), spans)

        return f(spans, i+1)

    spans = f([])

    ret = ['-'*(sum(map(lambda s: s+2, spans)) +1*len(hdr) +1)]
    ret.append('|' + '|'.join([' {{:{}}} '.format(y).format(x) for x,y in zip(hdr,spans)]) + '|')
    ret.append('-'*(sum(map(lambda s: s+2, spans)) +1*len(hdr) +1))

    def __f(lst, spans):
        if len(lst) == 0: return
        ret.append('|' + '|'.join([' {{:{}}} '.format(y).format(x) for x,y in zip(lst[0],spans)]) + '|')
        __f(lst[1:], spans)

    __f(recs, spans)

    ret.append('-'*(sum(map(lambda s: s+2, spans)) +1*len(hdr) +1))

    return '\n'.join(ret)

if __name__ == '__main__':
    print(prettyCSV('books.csv'))
    print(prettyCSV('languages.csv'))
