"""
File: So Doku Checker Solution
Author: Juan Diego Collazos
Date: 6/4/25
"""
from sys import stdin

N = 9
quadrant = [[ (i // 3) * 3 + (j // 3) for j in range(N)] for i in range(N)]

avail_row = [[ True for _ in range(N)] for _ in range(N)]
avail_col = [[ True for _ in range(N)] for _ in range(N)]
avail_quad = [[ True for _ in range(N)] for _ in range(N)]
fixed = [[ True for _ in range(N)] for _ in range(N)]
ans = 0

def check(row, col, val):
  quad = quadrant[row][col]
  return avail_row[row][val] and avail_col[col][val] and avail_quad[quad][val]

def tick(row, col, val, mark):
  quad = quadrant[row][col]
  avail_row[row][val] = mark
  avail_col[col][val] = mark
  avail_quad[quad][val] = mark

def backtrack(i, j):
  global ans
  if j == N:
    ans += 1
  else:
    if i == N:
      backtrack(0, j + 1)
    elif fixed[i][j]:
      backtrack(i + 1, j)
    else:
      val = 0
      while val < N and ans < 2:
        if check(i, j, val):
          tick(i, j, val, False)
          backtrack(i + 1, j)
          tick(i, j, val, True)
        val += 1

def main():
  global ans
  n_cases = 1
  row = list(map(int, stdin.readline().split()))
  while len(row) != 0:
    is_valid = True
    for i in range(N):
      for j in range(len(row)):
        val = row[j] - 1
        if val != -1:
          fixed[i][j] = True
          is_valid = is_valid and check(i, j, val)
          if is_valid: 
            tick(i, j, val, False)
      if i < N - 1:
        row = list(map(int, stdin.readline().split()))

    print("Case %d: " %(n_cases), end='')
    if not is_valid:
      print("Illegal.")
    else:
      ans = 0
      backtrack(0, 0)
      if ans == 0:
        print("Impossible.")
      elif ans == 1:
        print("Unique.")
      else:
        print("Ambiguous.")

    for i in range(N):
      for j in range(N):
        avail_row[i][j] = True
        avail_col[i][j] = True
        avail_quad[i][j] = True
        fixed[i][j] = False

    _white = stdin.readline()

    n_cases += 1
    row = list(map(int, stdin.readline().split()))

main()
