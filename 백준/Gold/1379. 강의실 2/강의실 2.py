import sys, heapq
input = sys.stdin.readline

N = int(input())

# room_list : 입력값
# room_cnt : 각 강의가 몇 번째 강의실에 들어갔는지 확인용
# queue : 강의실 시간 비교용 큐
# cnt : 최소 강의실 개수
room_list = []
room_cnt = [0] * (N+1)
queue = []
cnt = 0

for _ in range(N):
  num, start, end = map(int, input().split())
  room_list.append((num, start, end))

# 시작시간 기준으로 정렬
room_list = sorted(room_list, key=lambda x: x[1])

for num, start, end in room_list:
# 다음 강의 시작전에 강의가 끝났으면
# 해당 강의를 큐에서 빼기
  if queue and start >= queue[0][0]:
    room_cnt[num] = room_cnt[queue[0][2]]
    heapq.heappop(queue)

# 다음 강의 시작시간이 현재 큐에 들어가 있는 강의 중 가장 일찍 끝나는 강의보다 늦으면
# 강의실 개수를 하나 늘리기
  else:
    cnt += 1
    room_cnt[num] = cnt

# 위의 조건과 상관없이 반복문 한번당 강의 하나씩 큐에 추가
# 이 때는 시작 시간이 아닌 종료 시간을 정렬 기준으로 push
  heapq.heappush(queue, (end, start, num))

print(cnt)
for i in range(1, len(room_cnt)):
  print(room_cnt[i])  
