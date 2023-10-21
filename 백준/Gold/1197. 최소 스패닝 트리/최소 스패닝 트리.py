import sys
input = sys.stdin.readline


V, E = map(int, input().split())

# 입력받은 노드 정보를 가중치 순으로 정렬
num_list = [list(map(int, input().split())) for _ in range(E)]
num_list.sort(key=lambda x: x[2])

uf = [i for i in range(V+1)]
weight = 0

def find_parent(parent, i):
  if parent[i] != i:
    parent[i] = find_parent(parent, parent[i])
  return parent[i]


def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a < b:
    parent[b] = a
  else:
    parent[a] = b


for num in num_list:
  A, B, C = num

  if find_parent(uf, A) != find_parent(uf, B):
    union_parent(uf, A, B)
    weight += C
    
print(weight)