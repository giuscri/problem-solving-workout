import math

class qt_node:
    def __init__(self, color, childs=[]):
        self.color = color
        self.childs = childs

    def is_leaf(self):
        return len(self.childs) == 0

class quadtree:
    def __init__(self, lst):
        def f(lst):
            if 1 not in lst:
                return qt_node('black')
            elif 0 not in lst:
                return qt_node('white')

            llst = [[], [], [], []]

            size = int(math.sqrt(len(lst)))
            for i in range(0, size * size//2):
                if i % size < size//2:
                    llst[0].append(lst[i])
                else:
                    llst[1].append(lst[i])

            for i in range(size * size//2, size*size):
                if i % size < size//2:
                    llst[3].append(lst[i])
                else:
                    llst[2].append(lst[i])

            root = qt_node('gray')
            root.childs = [
                f(llst[0]),
                f(llst[1]),
                f(llst[2]),
                f(llst[3])
            ]

            return root
               

        self.root = f(lst)
        self.lst = lst

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

    def size(self): return self.count_leaves()

    def count(self):
        return len(self.lst)-self.size()

if __name__ == '__main__':
    lst = [0]*2+[1,0]+[0]*3+[1]*3+[0]*2+[1]*4
    q = quadtree(lst)
