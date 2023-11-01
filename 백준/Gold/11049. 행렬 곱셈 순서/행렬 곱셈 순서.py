import sys
input = sys.stdin.readline

N = int(input())

matrix_list = []

# 입력값 튜플 형태로 저장
for _ in range(N):
  r, c = map(int, input().split())
  matrix_list.append((r, c))

# 행렬 곱에 대한 처리를 진행할 이차원 테이블 생성
dp_list = [[0] * N for _ in range(N)]

# [i, i]를 기준으로 우측 상단의 테이블만 사용하기 때문에 l값이 증가하면 반복할 때 마다 필요한 row의 값이 감소
# 우하향 대각선으로 곱셈이 진행돼야 하기 때문에 col의 범위는 i와 같의 l의 영향을 받으면서 동시에 i의 영향을 받음
for l in range(N):
  for i in range(N-l-1):
    j = i + l + 1

    # 최솟값을 판별을 요구하기 때문에 초기값은 최대로
    dp_list[i][j] = sys.maxsize

    # i와 j의 중간 순회값인 k의 값에 따라 최솟값을 찾아내 현재 인덱스에 저장
    for k in range(i, j):
      dp_list[i][j] = min(dp_list[i][j], dp_list[i][k] + dp_list[k+1][j] + matrix_list[i][0] * matrix_list[k][1] * matrix_list[j][1])

print(dp_list[0][-1])