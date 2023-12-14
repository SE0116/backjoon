import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


# 두 대상의 부모 노드 합치기
def union(x, y, parent):
  x = find(x, parent)
  y = find(y, parent)

  if x < y:
    parent[y] = x
  else:
    parent[x] = y
  
# 현재 대상의 부모 노드 찾기
def find(x, parent):
  if parent[x] != x:
    parent[x] = find(parent[x], parent)
  
  return parent[x]
  

n, m = map(int, input().split())

set_list = []
for _ in range(m):
  set_list.append(list(map(int, input().split())))


parent = [i for i in range(n+1)]


for sets in set_list:
  # 첫 숫자가 0이면 합집합 만들기
  if sets[0] == 0:
    union(sets[1], sets[2], parent)
  
  # 첫 숫자가 1이면 두 수가 같인 집합안에 있는지 확인
  elif sets[0] == 1:
    if find(sets[1], parent) == find(sets[2], parent):
      print("YES")
    else:
      print("NO")