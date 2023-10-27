from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coin_list = []
for _ in range(N):
  coin_list.append(int(input()))


coin_list.sort(reverse=True)
queue = deque(coin_list)
cnt = 0

while queue:
  coin = queue.popleft()
  cnt += K // coin
  K = K % coin

print(cnt)