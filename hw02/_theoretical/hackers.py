dp = dict()

def phi(n):
  if n in dp:
    ans = dp[n]
  else:
    if n == 0: 
      ans = 0
    elif n == 1: 
      ans = max(H[n - 1], L[n - 1])
    else: 
      ans = max(phi(n - 1) + L[n - 1], phi(n - 2) + H[n - 1])
    dp[n] = ans
  return ans

L = [10, 20, 10, 10, 30]
H = [50, 60, 70, 20, 25]
N = len(L)

ans = phi(N)
print(ans)