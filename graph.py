G = {
    0: [2, 5],
    1: [2],
    2: [1, 0, 5, 3],
    3: [2, 6],
    4: [5],
    5: [2, 4, 0],
    6: [3],
    10: [12],
    11: [12],
    12: [10, 11],
}

def bfs(G, src):
    q = [src]
    visited = [src]
    while len(q) > 0:
        ppd = q.pop(0)
        for ad in G[ppd]:
            if ad in visited: continue
            visited.append(ad)
            q.append(ad)
    return visited

def connected_components(G):
    ret = []
    visited = []
    for v in G:
        if v in visited: continue
        cmpnt = bfs(G, v)
        for w in cmpnt:
            visited.append(w)
        ret.append(cmpnt)
    return ret
