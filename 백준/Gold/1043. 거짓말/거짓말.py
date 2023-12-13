import sys
input = sys.stdin.readline

# 같은 파티에 오는 사람들 묶기
def union(x, y, parent, reals):
  x = find(x, parent)
  y = find(y, parent)
  
  if x in reals:
    parent[y] = x
  elif y in reals:
    parent[x] = y
  else:
    if x < y:
      parent[y] = x
    else:
      parent[x] = y

# 부모 노드 찾기
def find(x, parent):
  if x != parent[x]:
    parent[x] = find(parent[x], parent)

  return parent[x]


N, M = map(int, input().split())

reals = list(map(int, input().split()))

# 진실을 아는 사람이 없으면 탐색하지 않고 모든 파티의 갯수 출력
if reals[0] == 0:
  print(M)
  exit()

parent = [i for i in range(N + 1)]
party_list = []

# 진실을 아는 사람과 파티에 오는 사람을 받을 때, 처음에 인원수가 먼저 주어지기 때문에
# 슬라이싱으로 처음으로 받는 수는 제외
for _ in range(M):
  party = list(map(int, input().split()))
  for i in range(1, party[0]):
    union(party[i], party[i + 1], parent, reals[1:])
  party_list.append(party[1:]) 

cnt = 0

# 파티에 진실을 아는 사람이 있으면 카운트 안하고 다음 파티로 넘어가기
for i in range(len(party_list)):
  for j in range(len(party_list[i])):
    if find(party_list[i][j], parent) in reals[1:]:
      break 

  else:
    cnt += 1

print(cnt)