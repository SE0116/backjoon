import sys
input = sys.stdin.readline


def dfs(length, idx):
  if length == 6:
    print(*subset)
    return

  for i in range(idx, N):
    subset.append(S[i])
    dfs(length + 1, i + 1)
    subset.pop()

while True:
  lotto = list(map(int, input().split()))

  if lotto[0] == 0:
    break
  
  S = lotto[1:]
  N = lotto[0]
  subset = []
  
  dfs(0, 0)

  print()