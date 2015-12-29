import functools
import math

class qt_node:
    def __init__(self, status, childs=[]):
        self.status = status
        self.childs = childs

    def is_leaf(self):
        return len(self.childs) == 0

class quadtree:
    def __init__(self, lst):
        def g(lst):
            size = int(math.sqrt(len(lst)))
            llst = [[] for i in range(4)]
            for i in range(0, size * size//2):
                if i%size < size//2:
                    llst[0].append(lst[i])
                else:
                    llst[1].append(lst[i])

            for i in range(size * size//2, size**2):
                if i%size < size//2:
                    llst[3].append(lst[i])
                else:
                    llst[2].append(lst[i])
            return llst

        def f(lst):
            if 1 not in lst:
                return qt_node('empty')
            elif 0 not in lst:
                return qt_node('full')
            llst = g(lst)
            root = qt_node('?')
            root.childs = [
                f(llst[0]),
                f(llst[1]),
                f(llst[3]),
                f(llst[2])
            ]
            return root

        self.root = f(lst)
        self.lst = lst

    @property
    def img(self):
        size = int(math.sqrt(len(self.lst)))
        return [[self.lst[i + j] for j in range(4)] for i in range(0, size**2, 4)]

    @property
    def inner_repr(self):
        def all_leaves(lst):
            lst = map(lambda x: x.is_leaf(), lst)
            return functools.reduce(lambda x,y: x and y, lst)

        def f(root):
            if root.is_leaf():
                return [root.status]
            elif all_leaves(root.childs):
                return list(map(lambda x: x.status, root.childs))
            else:
                lst = []
                for c in root.childs:
                    if c.is_leaf():
                        lst.append(c.status)
                    else:
                        lst.append(f(c))
                return lst
        
        return f(self.root)

    def count_leaves(self):
        def _count_leaves(root):
            if root.is_leaf():
                return 1
            cnt = 0
            for c in root.childs:
                if c.is_leaf():
                    cnt += 1
                else:
                    cnt += _count_leaves(c)
            return cnt

        return _count_leaves(self.root)

    @property
    def size(self): return self.count_leaves()

    def count(self):
        return len(self.lst)-self.size

if __name__ == '__main__':
    img0 = [0]*2+[1,0]+[0]*3+[1]*3+[0]*2+[1]*4
    img1 = [1]*12+[0]*4+[1]*12+[0]*4+[1]*12+[0]*4+[1]*12+[0]*4+ \
        [1]*8+[0,0]+[1]*14+[0,0]+[1]*14+[0,0]+[1]*14+[0,0]+ \
        [1]*6+[0]*8+[1,1,0,0]+[1]*4+[0]*8+[1,1,0,0]+[1]*4+ \
        [0]*8+[1,1,0,0]+[1]*4+[0]*8+[1,1,0,0]+[1]*4+[0]*14+ \
        [1]*2+[0]*14+[1]*2+[0]*13+[1]+[0]*14+[1]+[0]*3
    print(img0)
    q0 = quadtree(img0)
    print(q0.img)
    print(q0.inner_repr)
    print("vector size :- {0} quadtree size :- {1} saved space :- {2}".
    format(len(img0), q0.size, q0.count()))
    print(img1)
    q1 = quadtree(img1)
    print(q1.img)
    print(q1.inner_repr)
    print("vector size :- {0} quadtree size :- {1} saved space :- {2}".
    format(len(img1), q1.size, q1.count()))
