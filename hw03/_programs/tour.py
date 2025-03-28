from sys import stdin

MAX = 5001
INF = float('inf')

class DisjointSet:
  def __init__(self):
    self.p = [0 for i in range(MAX)]
    self.rango = [0 for i in range(MAX)]
    self.size = [1 for i  in range(MAX)]

  def reset(self, N):
    for i in range(N):
      self.makeSet(i)
  
  def makeSet(self, v):
    self.p[v], self.rango[v], self.size[v]  = v, 0, 1
  
  def findSet(self, v):
    ans = None
    if v == self.p[v]: ans = v
    else:
      self.p[v] = self.findSet(self.p[v])
      ans = self.p[v]
    return ans
  
  def lenght(self, u):
    return self.size[self.findSet(u)]
  
  def unionSet(self, u, v):
    u, v = self.findSet(u), self.findSet(v)
    if u != v:
      if self.rango[u] < self.rango[v]:
        u, v = v, u
      self.p[v] = u
      self.size[u] += self.size[v]
      self.size[v] = 0
      if self.rango[u] == self.rango[v]:
        self.rango[u] += 1
    return u

n = 0
d = DisjointSet()
G = [[] for i in range(MAX)]

def is_candidate(A):
  outside, inside = 0, INF
  i, ans = 0, True
  while i < n and ans:
    if d.findSet(i) == d.findSet(A):
      j = 0
      while j < len(G[i]) and ans:
        v, k = G[i][j]
        if d.findSet(v) == d.findSet(A):
          inside = min(inside, k)
        else:
          outside = max(outside, k)
        ans = inside > outside
        j += 1
    i += 1
  return ans

def kruskal(E):
  ans = 0
  d.reset(n)
  E.sort(reverse=True)
  for edge in E:
    _, u, v = edge
    set_u = d.findSet(u)
    set_v = d.findSet(v)
    if set_u != set_v:
      A = d.unionSet(set_u, set_v)
      if is_candidate(A):
        ans += d.lenght(A)
  return ans

def main():
  global n
  T = int(stdin.readline().strip())
  while T != 0:
    E = []
    n, m = map(int, stdin.readline().split())
    n += 1
    for _ in range(m):
      u, v, k = map(int, stdin.readline().split())
      G[u].append((v, k))
      G[v].append((u, k))
      E.append((k, u, v))
 
    print(kruskal(E))
    for i in range(n): G[i] = []
    T -= 1

main()