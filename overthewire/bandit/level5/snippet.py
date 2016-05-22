import os, stat

def traverse(root, cb, res=[]):
    for r in os.listdir(root):
        path = os.path.join(root, r)
        mode = os.stat(path).st_mode

        if stat.S_ISDIR(mode):
            traverse(path, cb, res)

        elif stat.S_ISREG(mode) and cb(path):
            res.append(path)

        else:
            # Not interested
            pass

    return res

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print('*** Usage: python3 snippet.py <path>')
        sys.exit(-1)

    def cb(path):
        mode = os.stat(path).st_mode

        if stat.S_IMODE(mode) & stat.S_IXUSR != 0:
            return False

        if os.stat(path).st_size != 1033:
            return False

        return True

    results = traverse(sys.argv[1], cb)

    assert len(results) > 0, '*** Nothing found.'

    print('*** Computed {}'.format(results[0]))
