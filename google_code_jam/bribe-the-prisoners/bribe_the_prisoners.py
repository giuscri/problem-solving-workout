#!/usr/bin/python3

def compute_costs(frm, to, to_free):
	if to_free == [] or to <= frm:
		return 0

	res = []

	for i in range(len(to_free)):
		costs = to - frm
		costs += compute_costs(frm, to_free[i] - 1, to_free[:i])
		costs += compute_costs(to_free[i] + 1, to, to_free[i + 1:])
		res.append(costs)

	return min(res)

if __name__ == '__main__':
	import sys

	T = int(sys.stdin.readline().strip())

	for i in range(1, T + 1):
		P, _ = map(int, sys.stdin.readline().strip().split(' '))

		to_free = list(map(int, sys.stdin.readline().strip().split(' ')))

		fmt = 'Case #{}: {}'
		costs = compute_costs(1, P, to_free)
		print(fmt.format(i, costs))
