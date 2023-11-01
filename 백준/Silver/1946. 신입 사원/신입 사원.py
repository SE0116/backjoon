import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):

  N = int(input())

  total_list = []

  # 지원자 순위를 입력받고 서류 순위대로 정렬
  for _ in range(N):
    docu, interview = map(int, input().split())
    total_list.append((docu, interview))

  total_list.sort()
  
  min_num = total_list[0][1]
  
  
  # 서류 순위가 1등인 지원자는 무조건 합격이기 때문에 1부터 시작
  pass_cnt = 1

  # 임의의 지원자의 면접 순위가 (앞에 정렬된 지원자들의 면접 순위 중 최솟값)보다 후순위면
  # 비교 대상의 합격 여부와 상관없이 서류, 면접 순위가 모두 밀리기 때문에 불합격
  for i in range(1, N):
    
    if total_list[i][1] > min_num:
      continue
    else:
      min_num = total_list[i][1]
      pass_cnt += 1

  print(pass_cnt)
