import sys
input = sys.stdin.readline


N, K = map(int, input().split())

item_list = list(map(int, input().split()))

multitap = []
result = 0

for i in range(K):
  # 이미 사용하려는 전기용품이 멀티탭에 꽂혀 있을 때
  if item_list[i] in multitap:
    continue

  # 아직 멀티탭에 꽂을 구멍이 있을 때
  if len(multitap) < N:
    multitap.append(item_list[i])

  # 멀티탭이 꽉 차있는데 꽂혀 잇는 전기용품들이 현재 사용하려는 것과 다를 때
  else:

    # change : 뺄 플러그의 위치
    # compare_idx : 아래 반복문에서 가장 나중에 쓸 전기용품 비교용 인덱스(인덱스로 가능한 값이 0부터이기 때문에 -1로 초기화)
    # compare_list : 앞으로 써야 할 전기용품의 목록
    change = 0
    compare_idx = -1
    compare_list= item_list[i:]
    result += 1

    # 멀티탭에 꽂힌 용품들이 이후에 언제 쓰이는지 확인
    for item in multitap:

      # 나중에 또 써야하면 target에 언제 쓰이는지 저장
      if item in compare_list:
        target = compare_list.index(item)
        
        # 이전에 저장된 값보다 최근에 저장된 값이 크면
        # 큰 값이 더 나중에 쓰인단 의미기 때문에 바꿔주기
        if compare_idx < target:
          compare_idx = target
          change = item

      # 다 쓴 전기용품이 있으면 그 자리에 다음으로 쓸 것 꽂기
      else:
        change = item
        break
    
    # 교체
    multitap[multitap.index(change)] = item_list[i]

print(result)