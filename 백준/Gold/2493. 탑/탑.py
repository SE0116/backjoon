import sys
input = sys.stdin.readline

N = int(input())

tower_list = list(map(int, input().split()))

stack = []
result = [0] * N

# 오른쪽부터 완전탐색 진행시 O(N^2)의 시간복잡도
# 따라서 왼쪽부터 스택을 이용해 탐색
for i in range(N):
  while stack:
    if stack[-1][1] > tower_list[i]:
      result[i] = stack[-1][0] + 1
      break

    else:
      stack.pop()

  stack.append((i, tower_list[i]))

print(*result)