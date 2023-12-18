# import bisect 사용 불가
from bisect import bisect_left
import sys
input = sys.stdin.readline


n = int(input())

ports = list(map(int, input().split()))
compare = []

for port in ports:
  if not compare or port > compare[-1]:
    compare.append(port)
  else:
    compare[bisect_left(compare, port)] = port

print(len(compare))