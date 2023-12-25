import sys
input = sys.stdin.readline


N = int(input())

bodies = []

for _ in range(N):
  weight, height = map(int, input().split())
  bodies.append((weight, height))

# 등수 저장용 배열
result = []

# 등수 계산기 끝날 때 마다 카운트 초기화
for body in bodies:
  cnt = 0

  # 키랑 몸무게가 둘 다 높으면 카운트 추가
  for i in range(N):
    if bodies[i][0] > body[0] and bodies[i][1] > body[1]:
      cnt += 1

  # cnt는 자신보다 덩치가 큰 사람의 명수이기 때문에 등수를 계산하기 위해서 +1
  result.append(cnt + 1)
  
print(*result)