from sys import stdin

N = 0
weapons = list()
dp = dict()

def belongs(u, X):
  return X | (1 << u) == X

def unitary(u, X):
  return X == (1 << u)

def remove(u, X):
  return X - (1 << u)

def union(X, Y):
  return X | Y

def universal(n):
  return (1 << n) - 1

def phi(u, X, W):
  key = (u, X, W)
  if key in dp:
    ans = dp[key]
  else:
    if not belongs(u, X):
      ans = 0
    elif unitary(u, X):
      ans = 1
    else:
      ans = 0
      Y = remove(u, X)
      for v in range(N):
        if belongs(v, Y) and belongs(v, W):
          ans += phi(v, Y, union(X, weapons[v]))
    dp[key] = ans
  return ans

def main():
  global N, weapons, dp
  i = 1
  n_cases = int(stdin.readline().strip())
  while i <= n_cases:
    N = int(stdin.readline().strip()) + 1
    weapons = []
    for _ in range(N):
      w = int(stdin.readline().strip()[::-1], 2) << 1
      weapons.append(w)

    ans = s = 0
    V, W = remove(s, universal(N)), weapons[s]
    for u in range(1, N):
      if belongs(u, W):
        ans += phi(u, V, union(W, weapons[u]))

    dp = dict()
    print("Case %d: %d" %(i, ans))
    i += 1

main()
