import sys, heapq

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

node_list = [[] for _ in range(N+1)]

for i in range(M):
  u, v = map(int, input().split())
  node_list[u].append(v)

node_dist = []
distance = [1e9] * (N+1)


def dijkstra(start):
  # 힙 선언 & 힙푸시
  queue = []
  heapq.heappush(queue, (0, start))
  distance[start] = 0

  # True 대신 힙 리스트가 True일때까지
  while queue:
    # heappop()
    dist, now = heapq.heappop(queue)
    
    # heappop으로 뺀 거리보다 작은 수가 이미 들어가있으면 넘기기
    if distance[now] < dist:
      continue
  
    # 다음 노드로 갈 수 있고, 최단거리가 더 짧은값으로 나오면 갱신
    for i in node_list[now]:
      cost = dist + 1
      if cost < distance[i]:
        distance[i] = cost
        heapq.heappush(queue, (cost, i))
      

dijkstra(X)

cnt = 0
for i in range(len(distance)):
  if distance[i] == K:
    print(i)
  else:
    cnt += 1

if cnt == len(distance):
  print(-1)