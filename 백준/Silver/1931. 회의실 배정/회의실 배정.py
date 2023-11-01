import sys
input = sys.stdin.readline

N = int(input())

meeting_list = []


for _ in range(N):
  start, end = map(int, input().split())
  meeting_list.append((start, end))

meeting_list = sorted(meeting_list, key=lambda x: (x[1], x[0]))
end_check = 0
cnt = 0

for start, end in meeting_list:
  if end_check <= start:
    end_check = end
    cnt += 1

print(cnt)