"""
File: Simple Minded Hashing
Author: Juan Diego Collazos
Date: 2/19/25
"""

from sys import stdin

ALPHA = 26
MAX_SUM = (ALPHA * (ALPHA + 1)) // 2

dp = [[[0 for k in range(ALPHA + 1)] for j in range(ALPHA + 1)] for i in range(MAX_SUM + 1)]

def bottom_up():
  dp[0][0][0] = 1
  for m in range(1, ALPHA + 1):
    for s in range(MAX_SUM + 1):
      for l in range(ALPHA + 1):
        dp[s][l][m] = dp[s][l][m - 1]
        if s >= m and l > 0:
          dp[s][l][m] += dp[s - m][l - 1][m - 1]

def main():
  i = 1
  bottom_up()
  L, S = map(int, stdin.readline().split())
  while L != 0 or S != 0:
    ans = 0
    if S <= MAX_SUM and L <= ALPHA:
      ans = dp[S][L][ALPHA]
    print("Case %d: %d" %(i, ans))
    L, S = map(int, stdin.readline().split())
    i += 1

main()