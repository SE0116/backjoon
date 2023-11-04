import sys
input = sys.stdin.readline

N, K = map(int, input().split())

num_list = list(map(int, input().strip()))
result = []


for i in range(N):
    # 스택에
    # K가 0이 되면 지울 숫자가 없음

    while result and num_list[i] > result[-1] and K > 0:
      result.pop()
      K -= 1

    result.append(num_list[i])

# 이렇게 출력하면 오답
# for i in range(len(result)):
#   print(result[i], end='')

# 주어진 숫자가 내림차순이면 pop이 안되고 K값이 떨어지지 않기 때문에
# 반복문이 끝나고 K값이 1 이상이면 슬라이싱을 사용하거나 K를 뺀 인덱스로 출력
# 아래 두 가지 중 하나 사용
for i in range(len(result)-K):
  print(result[i], end='')

# print(''.join(map(str, result[:N-K])))