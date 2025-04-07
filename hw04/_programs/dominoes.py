"""
File: The Dominoes Solitaire Solution
Author: Juan Diego Collazos
Date: 4/4/25
"""
from sys import stdin

MAX = 7
edge = [[ 0 for i in range(MAX)] for i in range(MAX)]

n, end = 0, 0
ans = False

def tick(u, v, val):
  edge[u][v] += val
  edge[v][u] += val

def backtrack(index, u):
  global ans
  if index == n:
    ans = u == end
  else:
    i = 0
    while i < len(edge[u]) and not ans:
      if edge[u][i] > 0:
        tick(u, i, -1)
        backtrack(index + 1, i)
        tick(u, i, 1)
      i += 1

def main():
  global ans, n, end
  n = int(stdin.readline().strip())
  while n != 0:
    m = int(stdin.readline().strip())
    _, start = map(int, stdin.readline().split())
    end, _ = map(int, stdin.readline().split())
    for _ in range(m):
      u, v = map(int, stdin.readline().split())
      tick(u, v, 1)

    ans = False
    backtrack(0, start)

    if ans: 
      print("YES")
    else: 
      print("NO")

    for i in range(MAX):
      for j in range(MAX):
        edge[i][j] = 0

    n = int(stdin.readline().strip())

main()