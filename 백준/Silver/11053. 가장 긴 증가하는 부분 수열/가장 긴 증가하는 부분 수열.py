import sys
input = sys.stdin.readline


N = int(input())

num_list = list(map(int, input().split()))

dp_list = [1] * N

for i in range(1, N):
  for j in range(0, i):
    if num_list[j] < num_list[i]:
      dp_list[i] = max( dp_list[i], dp_list[j]+1 )

print(max(dp_list))