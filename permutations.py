def permutations(l):
    if len(l) < 2:
        return [l]
    ret = []
    for i in range(len(l)):
        for p in permutations(l[:i] + l[i+1:]):
            ret.append([l[i]] + p)
    return ret

if __name__ == '__main__':
    ps = permutations([2,3,5,7])
