"""
File: The Settlers of Catan Solution
Author: Juan Diego Collazos
Date: 6/4/25
"""
from sys import stdin

MAX = 25
G = [[] for i in range(MAX)]
ans = 0
m = 0

def backtrack(path, visted):
  global ans
  i, u = 0, path[-1]
  ans = max(ans, len(path) - 1)
  while i < len(G[u]) and ans < m:
    v = G[u][i]
    if not visted[u][v]:
      path.append(v)
      visted[u][v] = visted[v][u] = True
      backtrack(path, visted)
      visted[u][v] = visted[v][u] = False
      path.pop()
    i += 1

def main():
  global m, ans
  n, m = map(int, stdin.readline().split())
  while n != 0:
    for i in range(m):
      u, v = map(int, stdin.readline().split())
      G[u].append(v)
      G[v].append(u)

    path = []
    ans, s = 0, 0
    visited = [[False for j in range(n)] for i in range(n)]
    while s < n and ans < m:
      path.append(s)
      backtrack(path, visited)
      path.pop()
      s += 1
    print(ans)

    for i in range(n): G[i] = []
    n, m = map(int, stdin.readline().split())


main()

