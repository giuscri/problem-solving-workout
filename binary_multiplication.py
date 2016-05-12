from functools import reduce

def from_lst_to_number(lst):
    assert reduce(lambda acc, el: acc and el, \
                     map(lambda el: el == 0 or el == 1, lst), True)

    return int(''.join(map(str, lst)), 2)

A = [1, 1, 0, 1, 1]
B = [1, 1, 1]

common_len = max(len(A), len(B))

while len(A) < common_len: A = [0] + A
while len(B) < common_len: B = [0] + B

m = [[ai & bi for ai in reversed(A)] for bi in reversed(B)]

C = 0
for shift_amount, r in enumerate(m):
    C += from_lst_to_number(r) << shift_amount

print('*** Computed C={}'.format(C))
