"""
File: Batman Solution
Author: Juan Diego Collazos
Date: 2/21/25
"""
from sys import stdin

INF = float('inf')

V, P = 0, 0

dp = dict()
powers, villains = [], []

def phi(p, v):
  if (p, v) in dp:
    ans = dp[p, v]
  else:
    if v == V: ans = 0
    elif p == P: ans = INF
    else:
      ans = phi(p + 1, v)
      if powers[p][0] >= villains[v][0] and p in villains[v][1]:
        ans = min(ans, powers[p][1] + phi(p + 1, v + 1))
    dp[p, v] = ans
  return ans

def main():
  global P, V, dp, powers, villains
  P, V, E = map(int, stdin.readline().split())
  while P != 0:
    name_powers = dict()
    for _ in range(P):
      name, attack, energy = stdin.readline().split()
      name_powers[name] = len(name_powers)
      powers.append((int(attack), int(energy)))
    for _ in range(V):
      _, defense, affect = stdin.readline().split()
      villains.append((int(defense), frozenset(map(lambda x : name_powers[x], affect.split(',')))))
    
    if E >= phi(0, 0):
      print("Yes")
    else:
      print("No")

    dp = dict()
    powers, villains = [], []

    P, V, E = map(int, stdin.readline().split())

main()