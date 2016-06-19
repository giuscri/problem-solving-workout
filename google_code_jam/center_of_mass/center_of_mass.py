#!/usr/bin/python3

import math

def compute_cm_and_its_velocity(lst):
	"""
	Compute the three components of
	the center of mass and its velocity
	splitted too in its three components
	"""
	x, y, z = 0., 0., 0.
	vx, vy, vz = 0., 0., 0.

	N = len(lst)
	for el in lst:
		x += el[0]
		y += el[1]
		z += el[2]

		vx += el[3]
		vy += el[4]
		vz += el[5]

	x = round(x * 1./N, 8)
	y = round(y * 1./N, 8)
	z = round(z * 1./N, 8)

	vx = round(vx * 1./N, 8)
	vy = round(vy * 1./N, 8)
	vz = round(vz * 1./N, 8)

	return x, y, z, vx, vy, vz

def compute_dmin_tmin(x, y, z, vx, vy, vz):
	numerator = round(- (x * vx + y * vy + z * vz), 8)
	denominator = round(vx**2 + vy**2 + vz**2, 8)

	try:
		tmin = round(numerator / denominator, 8)
	except ZeroDivisionError:
		tmin = -0. if numerator < 0 else 0.

	if tmin < 0.: tmin = -0.

	dmin_squared = \
		round((x + vx * tmin)**2, 8) \
		+ round((y + vy * tmin)**2, 8) \
		+ round((z + vz * tmin)**2, 8)

	dmin = math.sqrt(dmin_squared)

	return dmin, tmin

if __name__ == '__main__':
	import sys, re

	T = int(sys.stdin.readline().strip())

	for i in range(1, T + 1):
		N = int(sys.stdin.readline().strip())

		lst = []
		for l in range(N):
			res = list(map(int, sys.stdin.readline().strip().split(' ')))
			lst.append(res)

		x, y, z, vx, vy, vz = compute_cm_and_its_velocity(lst)
		dmin, tmin = compute_dmin_tmin(x, y, z, vx, vy, vz)

		print('Case #{}: {:.5f} {:.5f}'.format(i, dmin, tmin))
