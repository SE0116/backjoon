import sys
from collections import deque
input = sys.stdin.readline


num_computers = int(input())
num_pair = int(input())
cnt = 0

if num_pair != 0:
  # 입력받은 리스트 정렬

  pair_list = [list(map(int, input().split())) for _ in range(num_pair)]
  pair_list.sort(key=lambda pair_list: pair_list[0])
  if pair_list[0][0] != 1:
    pair_list.sort(key=lambda pair_list: pair_list[1])

  pair_list = deque(pair_list)
  queue = deque()
  sub_queue = deque()

  # 1번 컴퓨터가 시작지점이기 때문에 외부에서 저장 후 시작
  if num_computers != 1 and 1 in pair_list[0]:
    queue.append(1)

  loof_check = 0

  while pair_list and num_computers != 1:
    if 1 not in queue:
      break
    # 이미 queue 안에 둘 다 있으면 리스트에서 제외
    if pair_list[0][0] in queue and pair_list[0][1] in queue:
      pair_list.popleft()
      loof_check = 0
    
    # 둘 중 하나만 있으면 나머지 추가
    elif pair_list[0][0] in queue:
      queue.append(pair_list[0][1])
      pair_list.popleft()
      loof_check = 0

    elif pair_list[0][1] in queue:
      queue.append(pair_list[0][0])
      pair_list.popleft()
      loof_check = 0

    # 둘 다 없으면 후순위로 돌리기
    # 둘 다 없는 순서쌍이 한바퀴를 돌면 탈출
    else:
      if loof_check == len(pair_list):
        break
      if pair_list[0] in sub_queue:
        loof_check += 1
        pair_list.append(pair_list.popleft())
        continue
      sub_queue.append(pair_list[0])
      pair_list.append(pair_list.popleft())

  if num_computers != 1 and 1 in queue:
    for i in range(1, len(queue)):
      queue.popleft()
      cnt += 1

print(cnt)

