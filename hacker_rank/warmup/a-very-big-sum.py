import sys, re

_ = sys.stdin.readline();
lst = map(int, re.split(' ', sys.stdin.readline().strip()))
print(sum(lst))
