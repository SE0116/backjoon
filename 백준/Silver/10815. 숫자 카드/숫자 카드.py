import sys
input = sys.stdin.readline


def bin_search(target, lst):
  # 양 끝 초기값 설정
  left, right = 0, N - 1

  while left <= right:
    # 중간값 설정
    mid = (left + right) // 2
    
    # 중간값보다 작으면 왼쪽을 탐색하고 반대면 오른쪽 탐색
    if target < lst[mid]:
      right = mid - 1
    elif target > lst[mid]:
      left = mid + 1
    else:
      return 1
  
  # 탐색이 끝날때까지 반환이 안되면 없는 카드로 간주하고 false 반환
  return 0

N = int(input())
# 탐색할 배열은 정렬해놓기
sanggeun = sorted(list(map(int, input().split())))
M = int(input())
cards = list(map(int, input().split()))
result = []

# 하나씩 탐색해서 true면 카드를 가지고 있는 거니까 1, false면 없는 거니까 0 저장
for card in cards:
  if bin_search(card, sanggeun):
    result.append(1)
  else:
    result.append(0)

print(*result)