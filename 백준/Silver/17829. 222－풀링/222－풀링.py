import sys
input = sys.stdin.readline


# 2x2 배열에서 두 번째로 큰 수 반환
def check(lst, row, col):
  check_list = [lst[row][col], lst[row+1][col], lst[row][col+1], lst[row+1][col+1]]
  check_list.sort(reverse=True)
  return check_list[1]

def pooling(N, x, y):
  # 재귀로 배열의 길이가 2가 됐을 때 check 함수 호출
  if N == 2:
    return check(num_list, x, y)
  
  # 재귀에 쓸 중간값 초기화
  mid = N // 2

  # 배열을 4분할 해서 다시 재귀 호출
  result = [pooling(mid, x, y), pooling(mid, x+mid, y), pooling(mid, x, y+mid), pooling(mid, x+mid, y+mid)]
  result.sort(reverse=True)
  return result[1]


N = int(input())

num_list = []

for _ in range(N):
  num_list.append(list(map(int, input().split())))

print(pooling(N, 0, 0))