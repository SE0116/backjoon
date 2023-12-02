import sys
input = sys.stdin.readline


# 입력받은 리스트가 아닌 찾고자 하는 값에 대해 이진 탐색
def bin_search(lst, target):
  # 시작과 끝을 1과 입력받은 리스트의 최댓값으로 초기화
  # 랜선의 길이는 0이 될 수 없기 때문에 0이 아닌 1로 초기화
  start, end = 1, max(lst)

  while start <= end:
    # mid : 이진 탐색용 중간값
    # cnt : mid로 각 랜선을 자를 때 나오는 랜선의 갯수
    mid = (start + end) // 2
    cnt = 0

    # 각 랜선을 잘라 얻은 랜선의 갯수 저장
    for num in lan:
      cnt += num // mid
    
    # 만약 cnt가 N보다 더 크면 길이가 더 길게 자른거니까 낮은 값으로 내려가서 다시 이진 탐색
    # 더 작으면 반대로 높은 값으로 올라가서 이진 탐색
    # 원하는 길이가 나왔다고 바로 중간값을 반환하면 에러 발생
    if cnt >= target:
      start = mid + 1
    elif cnt < target:
      end = mid - 1

  return end


K, N = map(int, input().split())

lan = []
for _ in range(K):
  lan.append(int(input()))

print(bin_search(lan ,N))