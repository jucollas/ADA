"""
File: Mega Man Missions Solution
Author: Juan Diego Collazos
Date: 23/2/25
"""
from sys import stdin

N = 0
weapons = list()
dp = dict()

def belongs(u, X):
  return X | (1 << u) == X

def remove(u, X):
  return X - (1 << u)

def union(X, Y):
  return X | Y

def universal(n):
  return (1 << n) - 1

def empty(X):
  return X == 0

def phi(X, W):
  key = (X, W)
  if key in dp:
    ans = dp[key]
  else:
    if empty(X):
      ans = 1
    else:
      ans = 0
      for v in range(1, N):
        if belongs(v, X) and belongs(v, W):
          ans += phi(remove(v, X), union(W, weapons[v]))
    dp[key] = ans
  return ans

def main():
  global N, weapons, dp
  i = 1
  n_cases = int(stdin.readline().strip())
  while i <= n_cases:
    N = int(stdin.readline().strip()) + 1
    weapons = []
    for _ in range(N):
      weapons.append(int(stdin.readline().strip()[::-1], 2) << 1)

    s = 0
    V, W = remove(s, universal(N)), weapons[s]
    ans = phi(V, W)
    print("Case %d: %d" %(i, ans))

    dp = dict()
    i += 1

main()
