import sys
input = sys.stdin.readline

N = int(input())

# 두 자리수까지는 전부 한수로 취급
if N < 100:
  print(N)

else:
  cnt = 0
  # N부터 하나씩 줄여가면서 for문이 정상적으로 끝까지 실행될때만 한수로 취급
  while N != 0:
    N = str(N)
    for i in range(len(N)-2):
      if (int(N[i]) - int(N[i+1])) != (int(N[i+1]) - int(N[i+2])):
        break
    else:
      cnt += 1
    N = int(N)-1
  print(cnt)