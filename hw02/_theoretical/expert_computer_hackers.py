
dp = dict()
N = 0
L, H = list(), list()

def phi(n, b):
  if (n, b) in dp:
    ans = dp[n, b]
  else:
    if n == N:
      ans = 0
    else:
      value = max(L[n], H[n]) if b else L[n]
      ans = max(phi(n + 1, True), phi(n + 1, False) + value)
    dp[n, b] = ans
  return ans

def fi(n, b):
  if (n, b) in dp:
    ans = dp[n, b]
  else:
    if n == 0:
      ans = 0
    else:
      ans = fi(n - 1, True)
      if b: 
        ans = max(ans + L[n - 1], fi(n - 1, False) + H[n - 1])
    dp[n, b] = ans
  return ans

def phi2(n):
  if n in dp:
    ans = dp[n]
  else:
    if n == 0: ans = 0
    elif n == 1: ans = max(H[n - 1], L[n - 1])
    else: ans = max(phi2(n - 1) + L[n - 1], phi2(n - 2) + H[n - 1])
    dp[n] = ans
  return ans

def max_revenue(a, h, n):
    if n == 0:
        return 0
    if n == 1:
        return max(a[0], h[0])
    
    return max(max_revenue(a, h, n-1) + a[n-1], 
               max_revenue(a, h, n-2) + h[n-1], 
               max_revenue(a, h, n-1))


L = [10, 20, 10, 10, 30]
H = [50, 60, 70, 20, 25]
ans = phi2(5)
print(ans)

def main():
  global L, H, N, dp
  L = [10, 1, 10, 10]
  H = [5, 50, 5, 1]
  N = len(L)
  ans = phi(0, True)
  print(ans)
  dp = {}
  ans2 = fi(N, True)
  print(ans2)
  print(max_revenue(L, H, N))