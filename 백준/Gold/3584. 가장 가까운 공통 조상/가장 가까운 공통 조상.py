import sys
input = sys.stdin.readline


def find(x, parents):
  # x를 미리 넣지 않으면 본인이 부모 노드인 경우가 탐색이 안됨
  parent = [x]

  # x의 부모, 조상 노드들 전부 넣기
  while parents[x]:
    parent.append(parents[x])
    x = parents[x]

  return parent


T = int(input())

for _ in range(T):

  N = int(input())

  parents = [0] * (N+1)
  
  # 부모 노드가 몇 번째 인덱스인지 정리
  for _ in range(N-1):
    parent, child = map(int, input().split())
    parents[child] = parent

  A, B = map(int, input().split())

  # 마지막에 입력받은 값들의 부모, 조상 노드 정리
  parents_A = find(A, parents)
  parents_B = find(B, parents)

  # 공통 조상을 찾으려면 높이가 맞아야 하므로 더 아래 있는 노드의 높이 올려주기
  idx_A, idx_B = len(parents_A), len(parents_B)
  if idx_A > idx_B:
    idx_A, idx_B = idx_A - idx_B, 0
  else:
    idx_A, idx_B = 0, idx_B - idx_A
  
  # 같은 줄의 부모나 조상이 다를 때 다음 조상으로 넘어가기
  while parents_A[idx_A] != parents_B[idx_B]:
    idx_A += 1
    idx_B += 1

  print(parents_A[idx_A])