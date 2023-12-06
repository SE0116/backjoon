import sys
input = sys.stdin.readline


N, M = map(int, input().split())

miro = []

for _ in range(N):
  miro.append(list(map(int, input().split())))

visited = [[0] * M for _ in range(N)]
visited[0][0] = 1

if N < 2:
  print(sum(miro[0]))
  exit()

if M < 2:
  result = 0
  for i in range(N):
    result += miro[i][0]
  print(result)
  exit()

for row in range(0, N-1):
  for col in range(0, M-1):
    if not visited[row+1][col]:
      miro[row+1][col] = miro[row][col] + miro[row+1][col]
      visited[row+1][col] = 1

    if not visited[row][col+1]:
      miro[row][col+1] = miro[row][col] + miro[row][col+1]
      visited[row][col+1] = 1

    if not visited[row+1][col+1]:
      miro[row+1][col+1] = max(miro[row][col], miro[row+1][col], miro[row][col+1]) + miro[row+1][col+1]
      visited[row+1][col+1] = 1

print(miro[-1][-1])