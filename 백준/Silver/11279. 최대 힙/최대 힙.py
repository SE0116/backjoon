import sys, heapq

input = sys.stdin.readline

N = int(input())


x_queue = []
x_list = [int(input()) for _  in range(N)]

for i in range(N):
  if x_list[i] == 0:
    if not x_queue:
      print(0)
    else:
      print(-heapq.heappop(x_queue))
  else:
    heapq.heappush(x_queue, -x_list[i])