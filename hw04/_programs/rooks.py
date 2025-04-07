"""
File: Rooks Solution
Author: Juan Diego Collazos
Date: 6/4/25
"""
from sys import stdin

N = 15
INF = float('inf')

n, m = 0, 0
board = []
ans = INF
mask_bit = [ 1 << i for i in range(N)]

def check(mask, rooks):
  i, cnt = 0, 0
  while i < m and cnt <= rooks:
    if mask & mask_bit[i]:
      cnt += 1
    i += 1
  return cnt <= rooks

def backtrack(row, rooks, mask):
  global ans
  if row == n:
    if check(mask, rooks):
      ans = min(rooks, ans)
  elif rooks < ans:
    backtrack(row + 1, rooks + 1, mask)
    backtrack(row + 1, rooks, mask | board[row])

def main():
  global board, ans, n, m
  line = stdin.readline().strip()
  while line != 'END':
    board = []
    for _ in range(N):
      row = 0 
      for i in range(len(line)):
        if line[i] == '#':
          row = row | mask_bit[i]
      if row != 0:
        board.append(row)
      line = stdin.readline().strip()

    n, m = len(board), N
    ans = INF
    backtrack(0, 0, 0)
    print(ans)
main()



    




    