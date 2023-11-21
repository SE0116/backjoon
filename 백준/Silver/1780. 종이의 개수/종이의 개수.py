import sys
input = sys.stdin.readline


def cut(lst):
  # 리스트 슬라이싱을 위한 변수 선언
  cut_num = len(lst)//3

  # 숫자가 하나만 나올 때까지 들어가면 비교할 숫자가 없기 때문에 해당 값 +1
  if len(lst) == 1:
   cnt[lst[0][0]] += 1
   return
  # 비교군
  check = lst[0][0]
  
  cnt_num = 0

  for row in range(len(lst)):
    for col in range(len(lst)):
      # 시작점의 숫자와 다른 수가 나오면 9분할로 재귀탐색
      if check != lst[row][col]:
        cut([lst2[:cut_num] for lst2 in lst[:cut_num]])
        cut([lst2[:cut_num] for lst2 in lst[cut_num:cut_num * 2]])
        cut([lst2[:cut_num] for lst2 in lst[cut_num * 2:cut_num * 3]])
        
        cut([lst2[cut_num:cut_num * 2] for lst2 in lst[:cut_num]])
        cut([lst2[cut_num:cut_num * 2] for lst2 in lst[cut_num:cut_num * 2]])
        cut([lst2[cut_num:cut_num * 2] for lst2 in lst[cut_num * 2:cut_num * 3]])
      
        cut([lst2[cut_num * 2:cut_num * 3] for lst2 in lst[:cut_num]])
        cut([lst2[cut_num * 2:cut_num * 3] for lst2 in lst[cut_num:cut_num * 2]])
        cut([lst2[cut_num * 2:cut_num * 3] for lst2 in lst[cut_num * 2:cut_num * 3]])
        
        # break 사용시 불필요한 카운트가 더쌓이니 주의
        return
      
      cnt_num += 1
  # 모든 칸이 같은 숫자면 결과를 출력할 리스트에 한 장 추가
  # 처음 리스트 슬라이싱을 할 때 3으로 나눴다고 *3을 하면 틀림
  if cnt_num == len(lst) ** 2:
    cnt[lst[0][0]] += 1


N = int(input())

paper = []

for _ in range(N):
  paper.append(list(map(int, input().split())))

# (0, 1, -1) 숫자가 적힌 종이의 갯수
cnt = [0] * 3

cut(paper)

# -1, 0, 1 순서로 출력하기 위해 range를 아래와 같이 선언
for i in range(-1, 2, 1):
  print(cnt[i])