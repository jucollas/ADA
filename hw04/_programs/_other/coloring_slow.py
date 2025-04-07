"""
File: Graph Coloring Slow Solution
Author: Juan Diego Collazos
Date: 4/4/25
"""
from sys import stdin

MAX = 100
G = [[] for i in range(MAX)]
colorig = [False for i in range(MAX)]
ans = []
n = 0

def has_black_neighbors(u):
  i, ans = 0, False
  while i < len(G[u]) and not ans:
    ans = colorig[G[u][i]]
    i += 1
  return ans

def backtrack(node, black_node):
  global ans
  if node == n:
    if len(ans) < len(black_node):
      ans = black_node.copy()
  else:
    i = node
    while i < n:
      if not has_black_neighbors(i):
        colorig[i] = True
        black_node.append(i)
        backtrack(i + 1, black_node)
        colorig[i] = False
        black_node.pop()
      i += 1
    backtrack(i, black_node)

def main():
  global ans, n
  m = int(stdin.readline().strip())
  while m != 0:
    n, k = map(int, stdin.readline().split())
    for _ in range(k):
      u, v = map(int, stdin.readline().split())
      u -= 1; v -= 1
      G[u].append(v)
      G[v].append(u)
    ans = []
    backtrack(0, [])
    print(len(ans))
    print(' '.join(list(map(lambda x: str(x + 1), ans))))
    for i in range(n): G[i] = []
    m -= 1

main()

