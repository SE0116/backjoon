import sys
input = sys.stdin.readline


N = int(input())


line = []

for _ in range(N):
  x, y = map(int, input().split())
  line.append((x, y))

# 시작점 기준으로 오름차순 정렬
line.sort()

# 비교군을 첫 번째 입력받은 값으로 놓고 길이를 저장할 cnt 선언
check = [line[0][0], line[0][1]]
cnt = 0

for i in range(1, N):
  # x값을 기준으로 정렬돼있기 때문에 y값, 즉 끝 지점이 비교군보다 작기만 하면 추가적이 계산 X
  if line[i][1] <= check[1]:
    continue

  # 선이 걸쳐있는 경우에는 삐져나온 길이만큼만 합쳐주기
  elif line[i][0] <= check[1] < line[i][1]:
    check[1] = line[i][1]
  
  # 아예 벗어나있는 경우 측정하던 길이를 cnt에 저장하고 다음 선부터 다시 측정 시작
  else:
    cnt += check[1] - check[0]
    check = [line[i][0], line[i][1]]

print(cnt + (check[1] - check[0]))