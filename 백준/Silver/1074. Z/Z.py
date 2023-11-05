import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

cnt = 0

while N != 0:
  N -= 1
  size = 2 ** N
  
  # 제 2 사분면
  if r < size and c < size:
    pass
  
  # 제 1 사분면
  elif r < size and c >= size:
    cnt += size * size
    c -= size
  
  # 제 3 사분면
  elif r >= size and c < size:
    cnt += size * size * 2
    r -= size

  # 제 4 사분면
  else:
    cnt += size * size * 3
    r -= size
    c -= size

print(cnt)
    