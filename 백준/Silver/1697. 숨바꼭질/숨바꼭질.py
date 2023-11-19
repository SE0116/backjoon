from collections import deque
import sys
input = sys.stdin.readline


N, K = map(int, input().split())
queue = deque()
if N > K:
  check = [0] * (N + 1)

else: 
  check = [0] * ((K * 2) + 1)
queue.append((N, 0))
check[N] = 1

while queue:
  num, cnt = queue.popleft()
  if num == K:
    print(cnt)
    break
  
  if num < K:
    if check[num * 2] != 1:
      queue.append((num * 2, cnt + 1))
      check[num * 2] = 1

    if check[num + 1] != 1:
      queue.append((num + 1, cnt + 1))
      check[num + 1] = 1

  if  num - 1 >= 0 and check[num - 1] != 1:  
    queue.append((num - 1, cnt + 1))
    check[num - 1] = 1