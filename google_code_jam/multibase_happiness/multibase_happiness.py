from bases import Bases
from functools import reduce
from json import loads, dumps

"""
A bruteforce approach has
been enough to compute the
solution for the small input
-- something like 5minutes to
compute the total output.

For the large output the approach
is not feasible. It's likely
some mathematical property
of these magic's can be leveraged.

Maybe I'll come back to this
problem and thinking about it
again.
"""

CACHE = set()
def happy(n, b, lst):
	if (n, b) in CACHE:
		return True 

	if n in lst:
		return False

	s = Bases().toBase(n, b)
	if sum(map(lambda x: int(x)**2, s)) == 1:
		CACHE.add((n, b))
		return True

	return happy(sum(map(lambda x: int(x)**2, s)), b, lst + [n])

def smallest_happy_in(bs, happy_numbers):
	folder = lambda fltrd, b: filter(lambda z: z in happy_numbers[b], fltrd)
	try:
		return next(reduce(folder, bs[1:], happy_numbers[bs[0]]))
	except StopIteration:
		return 'UNKNOWN'

if __name__ == '__main__':
	from os.path import isfile
	import sys

	file_exists = isfile('happy_numbers.json')
	if file_exists:
		with open('happy_numbers.json') as f:
			happy_numbers = \
				dict(map(lambda p: (int(p[0]), p[1]), loads(f.read().strip()).items()))

	else:
		happy_numbers = {}
		for b in range(2, 10 + 1):
			for n in range(2, 50000):
				if happy(n, b, []):
					if b not in happy_numbers:
						happy_numbers[b] = []

					happy_numbers[b].append(n)

		with open('happy_numbers.json', 'w') as f:
			f.write(dumps(happy_numbers))

	T = int(sys.stdin.readline().strip())

	for i in range(1, T + 1):
		bs = tuple(map(int, sys.stdin.readline().strip().split(' ')))
		print('Case #{}: {}'.format(i, smallest_happy_in(bs, happy_numbers)))
