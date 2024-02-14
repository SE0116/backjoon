import sys
input = sys.stdin.readline


def bridge(n, m):
  dp_list = [[0 for _ in range(m + 1)] for _ in range(n + 1)] 
  
  for i in range(1, m + 1):
    dp_list[1][i] = i
 
  for i in range(2, n + 1): 
    for j in range(i, m + 1):
      for k in range(j, i - 1, -1):
        dp_list[i][j] += dp_list[i-1][k-1]
 
  return dp_list[n][m]


T = int(input())
for _ in range(T):
  N, M = map(int, input().split())
  print(bridge(N,M))