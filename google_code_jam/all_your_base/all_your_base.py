#!/usr/bin/python3

import string

def compute_map(s, m):
	if s == '':
		r = {}
		for k, v in m.items():
			if v < 10:
				r[k] = str(v)
			elif (v - 10) < 26:
				r[k] = string.printable[10:10+26][v - 10]
			else:
				raise Exception('Map m={} cannot be used'.format(m))

		return r

	for i in range(0, 36):
		if s[0] in m: continue
		if i in m.values(): continue
		m[s[0]] = i
		break

	return compute_map(s[1:], m)

def map_string(s, m):
	try:
		return ''.join(map(lambda x: m[x], s))
	except KeyError:
		print('Map m={} cannot translate s={}'.format(m, s))

def find_best_translation(s):
	for b in range(2, 36 +1):
		try:
			return int(s, b)
		except ValueError: pass

	raise Exception("Couldn't find a valid base to use.")

if __name__ == '__main__':
	import sys, re

	T = int(sys.stdin.readline().strip())

	for i in range(1, T + 1):
		s = sys.stdin.readline().strip()
		m = { s[0]: 1 }
		m = compute_map(s[1:], m)
		s = map_string(s, m)
		print('Case #{}: {}'.format(i, find_best_translation(s)))
