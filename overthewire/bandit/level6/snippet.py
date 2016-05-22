import os, stat

def traverse(root, cb, res=[]):
    if root == '/proc': return res

    try:
        rs = os.listdir(root)
    except PermissionError:
        return res

    for r in os.listdir(root):
        path = os.path.join(root, r)
        mode = os.stat(path, follow_symlinks=False).st_mode

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
        import pwd

        statinfo = os.stat(path, follow_symlinks=False)

        if statinfo.st_size != 33:
            return False

        if pwd.getpwuid(statinfo.st_uid).pw_name != 'bandit7':
            return False

        if pwd.getpwuid(statinfo.st_gid).pw_name != 'bandit6':
            return False

        return True

    results = traverse(sys.argv[1], cb)

    assert len(results) > 0, '*** Nothing found.'

    print('*** Computed {}'.format(results[0]))
