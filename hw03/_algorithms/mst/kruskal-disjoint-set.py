
MAX = 1000

class DisjointSet:
  def __init__(self):
    self.p = [0 for i in range(MAX)]
    self.rango = [0 for i in range(MAX)]

  def reset(self, N):
    for i in range(N):
      self.makeSet(i)
  
  def makeSet(self, v):
    self.p[v], self.rango  = v, 0
  
  def findSet(self, v):
    ans = None
    if v == self.p[v]: ans = v
    else:
      self.p[v] = self.findSet(self.p[v])
      ans = self.p[v]
    return ans
  
  def unionSet(self, u, v):
    u, v = self.findSet(u), self.findSet(v)
    if u != v:
      if self.rango[u] < self.rango[v]:
        u, v = v, u
      self.p[v] = u
      if self.rango[u] == self.rango[v]:
        self.rango[u] += 1

djSet = DisjointSet()

def kruskal(E : list, n):
  mst = []
  weight = 0

  djSet.reset(n)
  E.sort()

  for edge in E:
    k, u, v = edge
    if djSet.findSet(u) != djSet.findSet(v):
      mst.append(edge)
      weight += k
      djSet.unionSet(u, v)
      
  return mst, weight





  


