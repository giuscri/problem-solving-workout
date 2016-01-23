import re
import functools

with open('wordlist.txt') as f: ws = f.read().strip().split()

def ruzzles(grd, ws=ws):

    def f(grd, cn, cns):
        if len(cn) >= 3:
            cns.append(cn)
        r, c = cn[-1][0], cn[-1][1]

        room_north = r-1 >= 0 and (r-1,c) not in cn
        room_south = r+1 < len(grd) and (r+1,c) not in cn
        room_west = c-1 >= 0 and (r, c-1) not in cn
        room_east = c+1 < len(grd[0]) and (r, c+1) not in cn

        room = functools.reduce(lambda x,y: x or y, \
                                   [room_north, room_south, room_west, room_east])

        ## Exit condition here
        if not room: return

        if room_north: f(grd, cn + [(r-1, c)], cns)
        if room_south: f(grd, cn + [(r+1, c)], cns)
        if room_west: f(grd, cn + [(r, c-1)], cns)
        if room_east: f(grd, cn + [(r, c+1)], cns)

        return cns

    cns = []
    for r in range(len(grd)):
        for c in range(len(grd[0])):
            f(grd, [(r,c)], cns)

    _cns = []
    for cn in cns:
        _cns.append(''.join(list(map(lambda p, grd=grd: \
                                        grd[p[0]][p[1]], cn))))
    cns = _cns

    ws = filter(lambda w, grd=grd: \
              not re.search('[^{}]'.format(''.join(grd)), w), ws)

    return list(filter(lambda w: w in cns, ws))

if __name__ == "__main__":
    print(ruzzles(["walk", "moon", "hate", "rope"]))
    print(ruzzles(["abbr", "evia", "tion", "alba"]))
    print(ruzzles(["abse", "imtn", "nded", "ssen"]))
    print(ruzzles(["reca", "rwar", "aazp", "syon"]))
    print(ruzzles(["abst", "oime", "uesl", "snsp"]))
    print(ruzzles(["essx", "ndet", "sigh", "raen"]))
    print(ruzzles(["poap", "lkjh", "aswe", "jhnh"]))
