import sys
input = sys.stdin.readline


# 이진 탐색
def bin_search(num):
  left = 0
  right = len(result) - 1
  while left < right:
    mid = (left + right) // 2
    if result[mid] < num:
      left = mid+1
    else:
      right = mid
  return right


N = int(input())

wire = list(map(int, input().split()))
result = []

# 전깃줄 탐색
for i in range(N):
  if not result or result[-1] < wire[i]:
    result.append(wire[i])
  else:
    idx = bin_search(wire[i])
    result[idx] = wire[i]

print(N - len(result))