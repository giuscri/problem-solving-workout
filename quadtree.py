import math

class quadtree:
    def __init__(self, img):
        self.img = [
            [img[i+j] for j in range(int(math.log2(len(img))))]
                        for i in range(0, len(img), int(math.log2(len(img))))
        ]
    
    @property
    def inner_repr(self):
        def f(sq):
            print(sq)
            if len(list(filter(lambda x: x==0, sq))) == len(sq):
                return 'empty'
            if len(list(filter(lambda x: x==1, sq))) == len(sq):
                return 'full'
            
            res = []
            n = len(sq)
            mid = n//2
            res.append(f([sq[i][j] for i in range(0,mid) \
                                      for j in range(0,mid)]))
            res.append(f([sq[i][j] for i in range(0,mid) \
                                      for j in range(mid,n)]))
            res.append(f([sq[i][j] for i in range(mid,n) \
                                      for j in range(0,mid)]))
            res.append(f([sq[i][j] for i in range(mid,n) \
                                      for j in range(mid,n)]))
            return res
        return f(self.img)

if __name__ == '__main__':
    img0 =  [0]*2+[1,0]+[0]*3+[1]*3+[0]*2+[1]*4
    print(img0)
    q = quadtree(img0)
    print(q.img)
    print(q.inner_repr)
