import itertools

def compute_solution(lst, c):
    for comb in itertools.combinations(lst, r=2):
        if comb[0][1] + comb[1][1] == c:
            return (comb[0][0] + 1, comb[1][0] + 1)
    return tuple()

if __name__ == '__main__':
    fname = 'A-large-practice.in'
    with open(fname) as f:
        lines = f.read().strip().split('\n')
    
    ncases = int(lines[0])
    lines = lines[1:]

    for i in range(1, ncases + 1):
        c = int(lines[0])
        lines = lines[2:]

        lst = enumerate(map(int, lines[0].split(' ')))
        lst = list(lst)

        lines = lines[1:]
        r = compute_solution(lst, c)
        print('Case #{}: {}'.format(i, ' '.join(map(str, r))))
