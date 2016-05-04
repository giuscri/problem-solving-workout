import re
import math

def far(path):
    lst = map(lambda x: (x[0], int(x[1])), \
                 re.findall('[nsew][1-9]', path))
    d = { 'n': 0, 's': 0, 'e': 0, 'w': 0 }
    for k,v in lst: d[k] += v
    return math.sqrt((d['n'] - d['s'])**2 + (d['e'] - d['w'])**2)

if __name__ == "__main__":
    paths = ["w1e8n3w2", "s7n1w3w5e2", "n2w3s1e1",
             "n3w2s1e2", "n3w4e1n4w2e1w5s2n7"]

    for s in paths:
        print("The path \"{}\" corresponds to {:.2f} meters".format(s, far(s)))
