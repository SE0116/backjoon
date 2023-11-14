import sys
input = sys.stdin.readline


T = int(input())

fivemin = T // 300
T = T % 300

onemin = T // 60
T = T % 60 

tensec = T // 10
T = T % 10

if T:
  print(-1)
else:
  print(fivemin, onemin, tensec)