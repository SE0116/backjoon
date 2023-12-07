import sys
input = sys.stdin.readline


# 두 값을 비교해 작은 값을 부모 노드로
def union(x, y):
  x = find(x)
  y = find(y)

  if x == y:
    return
  
  if x > y:
    parent[x] = y
  else:
    parent[y] = x

# 부모 노드 찾기
def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]  



N = int(input())
M = int(input())

# 유니온 파인드용 배열
parent = [i for i in range(N)]

# 해당 도시에서 갈 수 있는 도시와 union 실행
for i in range(N):
  city = list(map(int, input().split()))
  for j in range(len(city)):
    if city[j] == 1:
      union(i, j)

schedule = list(map(int, input().split()))

parent = [-1] + parent
start = parent[schedule[0]]

# 부모 노드를 따라가다 끊기면 NO
# 끝까지 break 없이 쭉 가면 YES
for i in range(1, M):
  if parent[schedule[i]] != start:
    print("NO")
    break
else:
  print("YES")