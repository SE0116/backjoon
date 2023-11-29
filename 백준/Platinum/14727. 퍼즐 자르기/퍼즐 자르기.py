import sys
input = sys.stdin.readline


def rectangle(start, end):
  # 막대가 하나일 때 까지 분할했으면 해당 지점 높이 반환
  if start == end:
    return histogram[start]

  # 분할
  mid = (start + end) // 2

  # 현재 상태에서 중간 지점을 기준으로 양 옆으로 재귀 호출
  left_max = rectangle(start, mid)
  right_max = rectangle(mid + 1, end)

  # 가장 가운데 있는 두 개의 높이를 비교해 낮은 값을 기준으로 *2 ( 두 개의 직사각형이 가질 수 있는 넓이 )
  # 함수 초기에 막대가 하나일 때 높이를 반환하게 했기 때문에 에러 X
  left = mid
  right = mid + 1
  height_min = min(histogram[left], histogram[right])
  mid_max = height_min * 2

  # 탐색하는 길이가 히스토그램을 벗어나지 않는 선에서 탐색
  while left > start or right < end:
    # 오른쪽으로 더 탐색해도 히스토그램을 벗어나지 않고
    # 왼쪽으로 더 갈 수 없거나 왼쪽으로 갈 수 있어도 오른쪽으로 갔을 때의 높이가 더 클 때 오른쪽으로 탐색
    if right < end and (left == start or histogram[left - 1] < histogram[right + 1]):
      right += 1
      # 더 높이가 큰 직사각형은 이미 이전의 mid_max에서 계산됐기 때문에 더 낮은 높이를 height_min에 저장
      height_min = min(height_min, histogram[right])
    
    # 왼쪽으로 더 탐색해도 히스토그램을 벗어나지 않거나 ( OR)
    # 오른쪽으로 더 갈 수 없거나 오른쪽으로 갈 수 있어도 왼쪽으로 갔을 때의 높이가 더 클 때 왼쪽으로 탐색
    else:
      left -= 1
      height_min = min(height_min, histogram[left])

    # 직사각형의 길이를 한 칸 늘렸을 때 넓이와 기존에 저장된 최대 넓이 중 더 큰 수를 저장
    mid_max = max(mid_max, height_min * (right - left + 1))

  # 최종 최댓값 반환
  return max(left_max, right_max, mid_max)


N = int(input())

histogram = []

for _ in range(N):
  histogram.append(int(input()))

print(rectangle(0, N - 1))