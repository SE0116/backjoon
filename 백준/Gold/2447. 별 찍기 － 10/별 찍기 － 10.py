import sys
input = sys.stdin.readline

  
def star(N):
  # 입력받을 수 있는 N의 최솟값은 3이므로 베이스 케이스를 3으로 지정
  if N == 3:
    return ['***', '* *', '***']

  stars = star(N//3)
  star_list = []

  for st in stars:
    star_list.append(st * 3)

  for st in stars:
    star_list.append(st + ' ' * (N//3) + st )

  for st in stars:
    star_list.append(st * 3)

  return star_list


N = int(input())

print(*star(N), sep='\n')