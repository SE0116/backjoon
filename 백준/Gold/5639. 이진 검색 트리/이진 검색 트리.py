import sys
# RecursionError를 피하기 위해 재귀의 깊이를 추가로 지정
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def post_order(start, end):
  # 왼쪽 노드 범위가 오른쪽 범위를 넘어가면
  if start > end:
    return
  
  # mid : 왼쪽 서브트리와 오른쪽 서브트리를 나누는 기준
  # 모든 값이 루트 노드보다 작은 경우를 대비해 mid를 end + 1 로 초기화
  mid = end + 1

  # 부모  노드보다 자식노드의 값이 커지면
  for i in range(start + 1, end + 1):
    if node_list[start] < node_list[i]:
      # 이후 재귀로 들어갈 범위를 나누기 위해 더 큰 값을 mid로 초기화
      mid = i
      break

  # mid - 1 이 부모노드이기 때문에 이를 기준으로 왼쪽 / 오른쪽 서브트리로 나눠 재귀 진행
  post_order(start + 1, mid - 1)
  post_order(mid, end)
  print(node_list[start])

# 입력이 제대로 들어오지 않을 때 까지 node_list에 저장
node_list = []
while True:
  try:
    node_list.append(int(input()))

  except:
    break

# 배열의 인덱스 범위로 함수 호출
post_order(0, len(node_list) - 1)