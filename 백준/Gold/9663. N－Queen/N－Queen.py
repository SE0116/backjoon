def n_queens(row):
  global result

  # 퀸이 마지막 행까지 놓이면 +1
  if row == num_queens:
    result += 1
    return
  
  for i in range(num_queens):

    
    if visited[i] == False:
      board[row] = i

      if check_queens(row):
        visited[i] = True
        n_queens(row + 1)
        visited[i] = False

# 다른 퀸에 공격당하는 지 확인
def check_queens(idx):
  for i in range(idx):

    # 자신보다 윗 열에서 또는 대각선에서 공격하면 False
    if board[idx] == board[i] or  abs(idx-i) == abs(board[idx]-board[i]):
      return False

  return True

num_queens = int(input())

board = [0] * num_queens
visited = [False] * num_queens
result = 0

n_queens(0)
print(result)
