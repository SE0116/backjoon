import sys
input = sys.stdin.readline


A, B = map(int, input().split())
cnt =  1

while A < B:
  if B % 10 == 1:
    B //= 10

  elif B % 2:
    print(-1)
    exit()
    
  else:
    B //= 2
  cnt += 1

print(-1) if A > B else print(cnt)