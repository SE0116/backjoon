import sys
input = sys.stdin.readline

N, K = map(int, input().split())

dp_list = [[0] * (K+1) for _ in range(N+1)]
in_list = [(0, 0)]


for i in range(1, N+1):
  W, V = map(int, input().split())
  in_list.append((W, V))


for i in range(1, N+1):
  for j in range(1, K+1):
    if j < in_list[i][0]:
      dp_list[i][j] = dp_list[i-1][j]
    else:
      dp_list[i][j] = max(dp_list[i-1][j], in_list[i][1]  + dp_list[i-1][j-in_list[i][0]])
      
print(dp_list[N][K])