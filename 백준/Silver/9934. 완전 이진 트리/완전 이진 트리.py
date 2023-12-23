import sys
input = sys.stdin.readline


def tree(lst, idx):
  # 자식 노드가 없으면 현재 노드를 맞는 레벨에 저장
  if len(lst) == 1:
    result[idx].append(lst[0])
    return

  # 현재 리스트의 중간값이 부모 노드이기 때문에 현재 레벨에 저장
  mid = len(lst) // 2
  result[idx].append(lst[mid])

  # 다음 레벨에 있는 빌딩 탐색
  tree(lst[:mid], idx + 1)
  tree(lst[mid+1:], idx + 1)


K = int(input())

building = list(map(int, input().split()))
result = [[] for _ in range(K)]

tree(building, 0)

for i in range(K):
  print(*result[i])