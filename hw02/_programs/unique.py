"""
File: Unique World Solution
Author: Juan Diego Collazos
Date: 2/23/25
"""
from sys import stdin
from collections import deque

MAX = 100
INF = float("inf")

N = 0
G = [[] for _ in range(MAX)]
weight, road = dict(), []

def get_w(u, v):
  if v > u: u, v = v, u
  return weight[u, v]

def set_w(u, v, cost):
  if v > u: u, v = v, u
  weight[u, v] = cost

def bfs(s, t):
  dist = [ INF for _ in range(N)]; dist[s] = 0
  parents = [ -1 for _ in range(N)]
  q, found = deque([s]), False
  while len(q) != 0 and not found:
    u = q.popleft()
    if u == t: found = True
    else:
      for v, duv in G[u]:
        if dist[v] == INF:
          dist[v] = dist[u] + duv
          parents[v] = u
          q.append(v)
  return parents, dist[t]

def phi(S):
  n  = len(road)
  dp = [ INF for i in range(S + 1)]; 
  dp[0] = 0
  for i in range(n):
    val = road[i]
    for s in range(val, S + 1):
        dp[s] = min(dp[s], 1 + dp[s - val])
  return dp[S]

def read_data():
  data = []
  while len(data) == 0:
    data = stdin.readline().split()
  return int(data[0]) if len(data) == 1 else map(int, data)

def main():
  global N, weight, road
  n_cases = read_data()
  while n_cases != 0:
    N, M = read_data()
    for _ in range(M):
      u, v, cost = read_data(); u -= 1; v -= 1
      G[u].append((v, cost))
      G[v].append((u, cost))
      set_w(u, v, cost)

    K = read_data()
    for _ in range(K):
      u, v, cost = read_data(); u -= 1; v -= 1
      parents, dist = bfs(u, v)

      ans, S = INF, cost - dist
      if dist != INF and S >= 0 and S % 2 == 0:
        w, road = parents[v], []
        while parents[w] != -1:
          road.append(get_w(w, parents[w]))
          w = parents[w]

        ans = phi(S // 2) * 2 + len(road) + 1

      if ans != INF:
        print("Yes %d" %(ans))
      else:
        print("No")
    
    if n_cases > 1: 
      print()

    weight = dict()
    for i in range(N): G[i] = []
    n_cases -= 1

main()