'''
File: Rain Fall Solution
Author: Juan Diego Collazos
Date: 1/31/25
'''
from sys import stdin

eps = 1e-10

L, K, T1, T2 = 0, 0, 0, 0
loss_rain, k_mult_l = 0, 0

h = lambda v : v * T1 + (1/v) * k_mult_l - loss_rain

def bisection(f, v, a, b):
  low, hi  = a, b
  while abs(hi - low) > eps:
    mid = (hi + low) / 2
    if v <= f(mid): hi = mid
    else: low = mid
  ans = low
  return ans

def main():
  global L, K, T1, T2, loss_rain, k_mult_l
  n_cases = int(stdin.readline().strip())
  while n_cases > 0: 
    L, K, T1, T2, H = map(float, stdin.readline().split())
    if H < L:
      low = hi = H
    else:
      time_total = T1 + T2
      loss_rain = K * time_total
      k_mult_l = K * L

      a, b = 0, ((H + K * time_total) / T1)
      speed = bisection(h, H, a, b)
      rainfall = speed * T1
      if H == L:
        low, hi = L, rainfall
      else:
        low = hi = rainfall

    print("%.6f %.6f" %(low, hi))
    n_cases -= 1

main()