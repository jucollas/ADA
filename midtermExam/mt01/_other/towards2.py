from sys import stdin

INF = float("inf")
MAX = 30
MAX_NUMBER = 50
MAX_REMAINING = [MAX_NUMBER * i for i in range(2, MAX * 2)]
sign = {1, -1}

N = 0
board = []
dp = dict()

def phi(i, j, acum):
  key = (i, j, acum)
  if key in dp:
    return dp[key]

  ans = INF
  if i == 0 and j == 0:
    ans = abs(acum)
  else:
    if i > N - 1: 
      sub = [j, j + 1]
    else: 
      sub = []
      if j > 0: 
        sub.append(j - 1)
      if j < len(board[i]) - 1: 
        sub.append(j)

    for ind in sub:
      for val in sign:
        new_acum = acum + val * board[i - 1][ind]
        if abs(new_acum) < ans and new_acum <= MAX_REMAINING[i]:
          ans = min(ans, phi(i - 1, ind, new_acum))
  dp[key] = ans
  return ans

def main():
  global board, N, dp
  N = int(stdin.readline().strip())
  while N != 0:
    board = []
    for i in range(2 * N - 1):
      board.append(list(map(int, stdin.readline().split())))
    dp = dict()
    ans = phi(N * 2 - 2, 0, board[-1][0])
    print(ans)
    N = int(stdin.readline().strip())

main()

