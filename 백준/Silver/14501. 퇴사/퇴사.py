import sys
input = sys.stdin.readline


N = int(input())

consult = []  
for _ in range(N):
  T, P = map(int, input().split())
  consult.append([T, P])

dp_list = [0] * (N + 1)

for i in range(N-1, -1, -1):
  if consult[i][0] + i > N:
    dp_list[i] = dp_list[i + 1]
  
  else: dp_list[i] = max(dp_list[i + 1], dp_list[consult[i][0] + i] + consult[i][1])
  
print(dp_list[0])