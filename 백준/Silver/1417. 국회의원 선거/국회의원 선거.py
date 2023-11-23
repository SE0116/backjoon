import sys, heapq
input = sys.stdin.readline


N = int(input())
num1 = int(input())

candidate = []

for _ in range(N-1):
  n = int(input())
  heapq.heappush(candidate, (-n, n))

if len(candidate) == 0:
  print(0)
  exit()

cnt = 0

while candidate:
  top = heapq.heappop(candidate)[1]
  if num1 > top:
    break
  num1 += 1
  cnt += 1

  heapq.heappush(candidate, (-top + 1, top - 1))


print(cnt)