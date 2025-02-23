"""
File: Simple Minded Hashing
Author: Juan Diego Collazos
Date: 2/19/25
"""
from sys import stdin

ALPHA = 26
MAX_SUM = (ALPHA*(ALPHA + 1))//2

dp = [[[-1 for k in range(ALPHA + 1)] for j in range(ALPHA + 1)] for i in range(MAX_SUM + 1)]

def fi(s, l, m):
  if dp[s][l][m] != -1:
    ans = dp[s][l][m]
  else:
    if s == 0 and l == 0: ans = 1
    elif s == 0 or l == 0 or m == 0: ans = 0
    else:
      ans = fi(s, l, m - 1)
      if s >= m:
        ans += fi(s - m, l - 1, m - 1)
    dp[s][l][m] = ans
  return ans

def main():
  i = 1
  L, S = map(int, stdin.readline().split())
  while L != 0 or S != 0:
    ans = 0
    if S <= MAX_SUM and L <= ALPHA:
      ans = fi(S, L, ALPHA)
    print("Case %d: %d" %(i, ans))
    L, S = map(int, stdin.readline().split())
    i += 1

main()