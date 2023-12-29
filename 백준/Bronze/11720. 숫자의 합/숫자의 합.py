import sys
input = sys.stdin.readline


N = int(input())

nums = list(map(int, input().strip()))

result = 0

for num in nums:
  result += num

print(result)