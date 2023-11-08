import sys
input = sys.stdin.readline


def quad(y, x, n):
  # 각 영역의 첫 번째 숫자를 대조군으로 설정
  check = tree_list[y][x]

  # 각 영역을 순차적으로 돌면서 대조군과 다른 값이 발견되면 괄호를 열고 더 작은 영역에서 탐색
  for i in range(y, y+n):
    for j in range(x, x+n):
      if check != tree_list[i][j]:
        print('(', end='')
        quad(y, x, n//2)
        quad(y, x + n//2, n//2)
        quad(y + n//2, x, n//2)
        quad(y + n//2, x + n//2, n//2)
        print(')', end='')
        return

  if check == 0:
    print(0, end='')
  else:
    print(1, end='')


N = int(input())

tree_list = [list(map(int, input().strip())) for _ in range(N)]

quad(0, 0, N)