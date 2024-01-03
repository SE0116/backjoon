import sys
input = sys.stdin.readline


n, k = map(int, input().split())

coin = []

for _ in range(n):
  coin.append(int(input()))

dp_list = [0 for _ in range(k + 1)]
dp_list[0] = 1

for i in range(n):
  for j in range(coin[i], k + 1):
    if j - coin[i] >= 0:
      dp_list[j] += dp_list[j - coin[i]]

print(dp_list[k])
