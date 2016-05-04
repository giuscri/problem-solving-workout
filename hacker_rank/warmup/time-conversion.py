import re

def fn(s):
    PM = False
    if s[-2:] == 'PM':
        PM = True

    hh, mm, ss = map(int, re.split(':', s[:-2]))

    if hh == 12 and PM:
        return '{0:02}:{1:02}:{2:02}'.format(hh, mm, ss)

    if hh == 12 or PM:
        hh = (hh + 12) % 24

    return '{0:02}:{1:02}:{2:02}'.format(hh, mm, ss)

if __name__ == '__main__':
    assert fn('07:05:45PM') == '19:05:45'
    assert fn('13:05:45PM') == '01:05:45'
    assert fn('12:05:45AM') == '00:05:45'
    assert fn('12:05:45PM') == '12:05:45'

    import sys, re

    print(fn(sys.stdin.readline().strip()))
