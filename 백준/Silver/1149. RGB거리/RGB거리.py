import sys
input = sys.stdin.readline


N = int(input())

rgb_list = []
for _ in range(N):
  r, g, b = map(int, input().split())
  rgb_list.append([r, g, b])

# 이전 집까지 칠했을 때의 최솟값에 현재 집에서의 각 색의 비용을 더하기
for i in range(1, N):
  rgb_list[i][0] += min(rgb_list[i-1][1], rgb_list[i-1][2])
  rgb_list[i][1] += min(rgb_list[i-1][0], rgb_list[i-1][2])
  rgb_list[i][2] += min(rgb_list[i-1][0], rgb_list[i-1][1])

print(min(rgb_list[i]))