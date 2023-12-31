import sys
input = sys.stdin.readline


# 재귀 탐색
def dfs(length):
  # N개 만큼의 요소가 들어가면 출력하고 반환
  if length == N:
    print(*subset)
    return

  for i in range(1, N + 1):
    if i not in subset:
      # 현재 인덱스에 요소 넣기
      subset.append(i)
      # 다음 인덱스에 요소 넣기
      dfs(length + 1)
      # 한 번 순회가 끝나면 배열 비워주기
      subset.pop()

N = int(input())
subset = []

dfs(0)