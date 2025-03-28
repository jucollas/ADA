from sys import stdin
from heapq import heappop, heappush

MAX = pow(10, 6)
INF = float('inf')

N = 0
G = [[] for _ in range(MAX)]
T = [[] for _ in range(MAX)]

def dijkstra(s, G):
  dist = [INF] * N; dist[s] = 0
  pqueue = [(dist[s], s)]
  while len(pqueue) != 0:
    du, u = heappop(pqueue)
    if du == dist[u]:
      for v, duv in G[u]:
        if dist[v] > du + duv:
          dist[v] = du + duv
          heappush(pqueue, (dist[v], v))
  return dist

def main():
  global N
  n_cases = int(stdin.readline().strip())
  while n_cases != 0:
    N, M = map(int, stdin.readline().split())
    for i in range(M):
      u, v, duv = map(int, stdin.readline().split()); u-=1; v-=1
      G[u].append((v, duv))
      T[v].append((u, duv))
    
    ans = sum(dijkstra(0, G)) + sum(dijkstra(0, T))
    print(ans)

    for i in range(N): 
      G[i] = []
      T[i] = []
    n_cases -= 1

main()