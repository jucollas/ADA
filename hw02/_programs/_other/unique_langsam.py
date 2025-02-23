import sys
from sys import stdin
from collections import deque

sys.setrecursionlimit(100000)

MAX = 100
INF = float("inf")

G = [[] for _ in range(MAX)]
w, dp = dict(), dict()
I, n = 0, 0
road = []

def get_w(u, v):
  return w[max(u, v), min(u, v)]

def set_w(u, v, cost):
  w[max(u, v), min(u, v)] = cost

def bfs(s, t):
  visited = [ False ] * n; visited[s] = True
  parents = [ -1 ] * n
  q = deque([s])
  found = False
  while len(q) != 0 and not found:
    u = q.popleft()
    if u == t:
      found = True
    else:
      for v, _ in G[u]:
        if not visited[v]:
          q.append(v)
          visited[v] = True
          parents[v] = u
  return parents, found

"""def phi(i, s):
  if (i, s) in dp:
    ans = dp[i, s]
  else:
    if s == 0:
      ans = 0
    else:
      ans = INF
      if i > 0:
        ans = phi(i - 1, s)
        if s >= road[i - 1] * 2:
          ans = min(ans, 2 + phi(i, s - (road[i - 1]*2)))
    dp[i, s] = ans
  return ans"""

'''def phi(S):
  I = len(road)
  dp = [[INF for s in range(S+ 1)] for i in range(I + 1)]
  for i in range(I):
    dp[i][0] = 0

  for i in range(1, I+ 1):
    for s in range(S + 1):
      dp[i][s] = dp[i - 1][s]
      if s >= road[i - 1] * 2:
        dp[i][s] = min(dp[i][s], 2 + dp[i][s - road[i - 1] * 2])
  return dp[I][S]'''

def phi(i, s):
  if (i, s) in dp:
    ans = dp[i, s]
  else:
    if i == 0 and s == 0:
      ans = 0
    else:
      ans = INF
      if i > 0 and s >= road[i - 1]:
        ans = 1 + phi(i - 1, s - road[i - 1])
      if i < I and s >= road[i] * 2:
        ans = min(ans, 2 + phi(i, s - road[i] * 2))
    dp[i, s] = ans
  return ans

def read_data():
  data = []
  while len(data) == 0:
    data = stdin.readline().split()
  return int(data[0]) if len(data) == 1 else map(int, data)

def main():
  global I, w, road, n, dp
  n_cases = read_data()
  while n_cases != 0:
    n, m = read_data()

    for _ in range(m):
      u, v, cost = read_data(); u -= 1; v -= 1
      G[u].append((v, cost))
      G[v].append((u, cost))
      set_w(u, v, cost)

    k = read_data()
    for _ in range(k):
      u, v, cost = read_data(); u -= 1; v -= 1
      parents, found = bfs(u, v)
    
      if not found:
        ans = INF
      else:
        s, road = v, []
        while parents[s] != -1:
          road.append(get_w(s, parents[s]))
          s = parents[s]

        road.reverse()
        term = road.pop()
        road.sort()

        ans = INF
        if len(road) == 0 and cost == term:
          ans = 1
        elif term < cost:
          dp = dict()
          I, S = len(road), cost - term
          ans = phi(I, S) + 1

      if ans != INF:
        print("Yes %d" %(ans))
      else:
        print("No")
    
    if n_cases > 1: 
      print()

    w = dict()
    for i in range(n): G[i] = []
    n_cases -= 1

main()