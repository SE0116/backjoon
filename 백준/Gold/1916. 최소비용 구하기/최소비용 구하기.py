import sys, heapq
input = sys.stdin.readline


def dijkstra(start):
  queue = []
  heapq.heappush(queue, (0, start))
  distance[start] = 0

  while queue:
    d, idx = heapq.heappop(queue)

    if distance[idx] < d:
      continue

    for i in bus_list[idx]:
      total =  d + i[1]
      if distance[i[0]] > total:
        distance[i[0]] = total
        heapq.heappush(queue, (total, i[0]))


N = int(input())
M = int(input())

bus_list = [[] for _ in range(N+1)]

for i in range(M):
  start_num, end_num, pay = map(int, input().split())
  bus_list[start_num].append((end_num, pay))
start, end = map(int, input().split())

distance = [1e9] * (N + 1)

dijkstra(start)

print(distance[end])