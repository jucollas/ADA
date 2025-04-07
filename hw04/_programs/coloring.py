"""
File: Graph Coloring Solution
Author: Juan Diego Collazos
Date: 6/4/25
"""
from sys import stdin

MAX = 100
mask_bit = [ 1 << i for i in range(MAX)]

G = [mask_bit[i] for i in range(MAX)]
ans = []
n = 0

def can_be_colored(A, i):
  return A & mask_bit[i] == 0

def backtrack(node, coloring, black_node):
  global ans
  if node == n:
    if len(ans) < len(black_node):
      ans = black_node.copy()
  else:
    i = node
    while i < n:
      if can_be_colored(coloring, i):
        black_node.append(i)
        backtrack(i + 1, coloring | G[i], black_node)
        black_node.pop()
      i += 1
    backtrack(i, coloring, black_node)

def main():
  global ans, n
  m = int(stdin.readline().strip())
  while m != 0:
    n, k = map(int, stdin.readline().split())
    for _ in range(k):
      u, v = map(int, stdin.readline().split())
      u -= 1; v -= 1
      G[u] |= mask_bit[v]
      G[v] |= mask_bit[u]
    ans = []
    backtrack(0, 0, [])
    print(len(ans))
    print(' '.join(list(map(lambda x: str(x + 1), ans))))
    for i in range(n): G[i] = mask_bit[i]
    m -= 1

main()

