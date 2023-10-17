import sys
input = sys.stdin.readline

input_count = int(input())

word_list = [input().strip() for _ in range(input_count)]

word_set = list((set(word_list)))
word_cnt = [len(word_set[i]) for i in range(len(word_set))]
cnt_list = [0] * (max(word_cnt)+1)

# 단어의 크기별로 몇 개씩 있는지 개수 세기
for i in range(len(word_cnt)):
  for j in range(len(cnt_list)):
    if word_cnt[i] == j:
      cnt_list[j] += 1

# 퀵 정렬
def quick_sort(cnt, lst, left, right):
  pl, pr = left, right
  pivot = cnt[(left+right)//2]

  while pl <= pr:
    while cnt[pl] < pivot: pl += 1
    while cnt[pr] > pivot: pr -= 1

    if pl <= pr:
      cnt[pl], cnt[pr] = cnt[pr], cnt[pl]
      lst[pl], lst[pr] = lst[pr], lst[pl]
      pl += 1
      pr -= 1

  if left < pr: quick_sort(cnt, lst, left, pr)
  if right > pl: quick_sort(cnt, lst, pl, right)


quick_sort(word_cnt, word_set, 0, len(word_set)-1)


check, idx = 0, 1

while idx < len(cnt_list):
  
  if cnt_list[idx] == 0:
    idx += 1
    continue
  word_set[check:check+cnt_list[idx]] = sorted(word_set[check:check+cnt_list[idx]])
  check += cnt_list[idx]
  idx += 1

for i in range(len(word_set)):
  print(word_set[i])
