import sys
input = sys.stdin.readline


N = int(input())

time_list = sorted(list(map(int, input().split())))

total, result = 0, 0

for time in time_list:
  total += time
  result += total

print(result)