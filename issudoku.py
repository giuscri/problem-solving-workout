def ck_row(r):
    if len(r) != len(set(r)): return False
    return sorted(r) == list(range(1, 9 +1))

def ck_rows(lst):
    def f(lst):
        if len(lst) == 0: return True
        return ck_row(lst[0]) and f(lst[1:])
    return f(lst)

def ck_cols(lst):
    def f(i):
        if i == len(lst): return True
        def _f(lst, i, res=[]):
            if len(lst) == 0: return res
            res.append(lst[0][i])
            return _f(lst[1:], i, res)
        r = _f(lst, i)
        if not ck_row(r): return False
        return f(i+1)
    return f(0)

def ck_33(lst):
    def f(lst, res):
        if len(lst) == 0: return res
        return f(lst[1:], res + lst[0])
    r = f(lst, [])
    return ck_row(r)

def is_sudoku(lst):
    if not ck_rows(lst): return False
    if not ck_cols(lst): return False

    subs = (
        list(map(lambda l: l[:3], lst))[:3],
        list(map(lambda l: l[:3], lst))[3:6],
        list(map(lambda l: l[:3], lst))[6:],
        list(map(lambda l: l[3:6], lst))[:3],
        list(map(lambda l: l[3:6], lst))[3:6],
        list(map(lambda l: l[3:6], lst))[6:],
        list(map(lambda l: l[6:], lst))[:3],
        list(map(lambda l: l[6:], lst))[3:6],
        list(map(lambda l: l[6:], lst))[6:],
    )

    assert len(subs) == 9

    def f(lst):
        if len(lst) == 0: return True
        return ck_33(lst[0]) and f(lst[1:])

    return f(subs)

if __name__ == '__main__':

    s0 = [[2,7,6,3,1,4,9,5,8],
          [8,5,4,9,6,2,7,1,3],
          [9,1,3,8,7,5,2,6,4],
          [4,6,8,1,2,7,3,9,5],
          [5,9,7,4,3,8,6,2,1],
          [1,3,2,5,9,6,4,8,7],
          [3,2,5,7,8,9,1,4,6],
          [6,4,1,2,5,3,8,7,9],
          [7,8,9,6,4,1,5,3,2]]

    s1 = [[2,7,6,3,1,4,9,5,8],
          [8,5,4,9,6,2,7,1,3],
          [9,1,3,8,7,5,2,6,4],
          [4,6,8,1,2,7,3,9,5],
          [5,9,7,4,3,8,6,2,1],
          [3,2,5,7,8,9,1,4,6],
          [1,3,2,5,9,6,4,8,7],
          [6,4,1,2,5,3,8,7,9],
          [7,8,9,6,4,1,5,3,2]]

    s2 = [[2,7,6,3,1,4,9,5,8],
          [8,5,4,9,6,2,7,1,3],
          [9,1,3,8,7,5,2,6,4],
          [3,2,5,7,8,9,1,4,6],
          [6,4,1,2,5,3,8,7,9],
          [7,8,9,6,4,1,5,3,2],
          [3,2,5,7,8,9,1,4,6],
          [6,4,1,2,5,3,8,7,9],
          [7,8,9,6,4,1,5,3,2]]

    s3 = [[2,7,6,9,5,8,9,5,8],
          [8,5,4,7,1,3,7,1,3],
          [9,1,3,2,6,4,2,6,4],
          [4,6,8,3,9,5,3,9,5],
          [5,9,7,6,2,1,6,2,1],
          [1,3,2,4,8,7,4,8,7],
          [3,2,5,1,4,6,1,4,6],
          [6,4,1,8,7,9,8,7,9],
          [7,8,9,5,3,2,5,3,2]]

    print("s0 :-", is_sudoku(s0))
    print("s1 :-", is_sudoku(s1))
    print("s2 :-", is_sudoku(s2))
    print("s3 :-", is_sudoku(s3))
