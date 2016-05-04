import sys

lst = []
for i in range(2):
	lst.append(int(sys.stdin.readline().strip()))

print(sum(lst))
