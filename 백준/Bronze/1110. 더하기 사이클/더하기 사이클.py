import sys, copy
input = sys.stdin.readline

N = str(input()).strip('\n')

copyN = copy.deepcopy(N)

# 주어진 수가 10보다 작으면 앞에 0 붙이기 
if len(N) == 1:
  N = '0' + N

# 사이클 길이, 새로운 수를 저장할 new (입력값이 0이상 99이하이기 때문에 100으로 저장)
cnt = 0
new = 100

  
# 새로운 수 만들기
while int(new) != int(copyN):
  new = N[1] + str((int(N[0]) + int(N[1])) % 10)
  N = new
  cnt += 1
print(cnt)